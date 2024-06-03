from django.contrib import messages
from django.contrib.auth import logout, authenticate, login
from django.contrib.auth.hashers import check_password
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect
from django.core.exceptions import ObjectDoesNotExist
from datetime import date
from django.contrib.auth.models import User
from . import forms, models
from .forms import SearchForm
from .models import adminsignupmodel, Newbookmodel, studentsignupmodel, IssuedBook
from django.utils.http import urlencode
from django.contrib.auth.password_validation import validate_password
from django.core.exceptions import ValidationError

# Create your views here.
def index(request):
    return render(request, 'index.html')


def adminpage(request):
    return render(request, 'adminpage.html')


def studentpage(request):
    return render(request, 'studentpage.html')


def adminsignup(request):
    if request.method == 'POST':
        # Getting form data from the request
        firstname = request.POST.get('firstname')
        lastname = request.POST.get('lastname')
        email = request.POST.get('email')
        username = request.POST.get('username')
        password = request.POST.get('password')
        confirm_password = request.POST.get('confirm_password')

        # Check if the username already exists
        if User.objects.filter(username=username).exists():
            # Render the sign-up form with an error message
            error_message = "Username already taken. Please choose a different username."
            return render(request, 'adminsignup.html', {'error_message': error_message})

        # Create and save the AdminSignup object
        user = User.objects.create_user(first_name=firstname, last_name=lastname, email=email, username=username,
                                        is_staff=True, is_superuser=True)
        user.set_password(password)
        user.save()

        # Redirect to a success page or perform other actions
        return HttpResponseRedirect('adminsignin')  # Placeholder response

    else:
        # Render the sign-up form for GET requests
        return render(request, 'adminsignup.html')

def adminafterlogin(request):
    return render(request, 'adminafterlogin.html')


def adminsignin(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)
        if user is not None and user.is_active:
            if user.is_superuser and user.is_staff:
                login(request, user)
                return redirect(adminafterlogin)
        else:
            msg = "Invalid email or password"
            return render(request, 'adminsignin.html', {'msg': msg})

    return render(request, 'adminsignin.html')


def addbook(request):
    if request.method == 'POST':

        # Extract form data
        bookname = request.POST.get('bookname')
        author = request.POST.get('author')
        year = request.POST.get('year')
        category = request.POST.get('category')
        image = request.FILES.get('image')
        desc = request.POST.get('desc')
        shelfid = request.POST.get('shelfid')
        publisher = request.POST.get('publisher')

        if Newbookmodel.objects.filter(bookname=bookname, author=author).exists():
            # If the book already exists, display an error message
            messages.error(request, 'Book with the same name and author already exists.')
            return render(request, 'addbook.html')

        # Create a new instance of addbookmodel with the form data
        new_book = Newbookmodel(
            bookname=bookname,
            author=author,
            year=year,
            category=category,
            image=image,
            desc=desc,
            shelfid=shelfid,
            publisher=publisher

        )

        # Save the new book object to the database
        new_book.save()

        # Redirect to a success page or another appropriate URL
        return render(request, 'addbook.html', {
            "success": True
        })  # Change 'success_page' to the URL of your success page

    else:
        # Render the add book form for GET requests
        return render(request, 'addbook.html')


def viewbook(request):
    books = Newbookmodel.objects.all()  # Fetch all books from the database
    return render(request, 'viewbook.html', {"books": books})


def studentsignup(request):
    if request.method == 'POST':
        firstname = request.POST.get('firstname')
        lastname = request.POST.get('lastname')
        email = request.POST.get('email')
        username = request.POST.get('username')
        password = request.POST.get('password')
        cpassword = request.POST.get('confirm_password')
        if User.objects.filter(username=username).exists():
            return render(request, 'studentsignup.html', {'error': 'Username already exists.'})

        if cpassword == password:
            try:
                validate_password(password)
                user = User.objects.create_user(first_name=firstname, last_name=lastname, email=email, username=username)
                user.set_password(password)
                user.save()
                return render(request, 'studentlogin.html')
        # student_signup.save()
            except ValidationError as e:
                errors=e.messages
        # Redirect to a success page or perform other actions
                return render(request,'studentsignup.html',{'errors':errors})  # Placeholder response

    # else:
        # Render the sign-up form for GET requests
    return render(request, 'studentsignup.html')


def studentlogin(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None and user.is_active:
            login(request, user)
            return redirect(studentafterlogin)

        else:
            messages.error(request, "Invalid email or password")
            return redirect('studentlogin')
    return render(request, 'studentlogin.html')


def issuebook(request):
    # form=forms.IssuedBookForm()
    # if request.method=='POST':
    #     #now this form have data from html
    #     form=forms.IssuedBookForm(request.POST)
    #     if form.is_valid():
    #         obj=models.IssuedBook()
    #         obj.firstname=request.POST.get('firstname')
    #         obj.lastname=request.POST.get('lastname')
    #         obj.bookname = request.POST.get('bookname')
    #         obj.author = request.POST.get('author')
    #         obj.save()
    #         firstname = obj.firstname
    #         return render(request,'issuebook.html',{
    #             'firstname':firstname,
    #             'success':True

    #         })
    students = User.objects.filter(is_superuser=False, is_staff=False)
    books = Newbookmodel.objects.all()
    if request.method == "POST":
        student = request.POST.get('student')
        user_stud = User.objects.get(username=student)
        books = request.POST.get('book')
        book = Newbookmodel.objects.get(bookname=books)
        issuedate = date.today()
        issue_book = IssuedBook.objects.create(student=user_stud, book=book, issuedate=issuedate)
        issue_book.save()
        msg = "Issued Successfully!"
        return render(request, 'issuebook.html', {
            "success": True, 'user_stud': user_stud
        })
    return render(request, 'issuebook.html', {'students': students, 'books': books})


# def viewissuedbook_view(request):
#     issuedbooks=models.IssuedBook.objects.all()
#     li=[]
#     for ib in issuedbooks:
#         issdate=str(ib.issuedate.day)+'-'+str(ib.issuedate.month)+'-'+str(ib.issuedate.year)
#         expdate=str(ib.expirydate.day)+'-'+str(ib.expirydate.month)+'-'+str(ib.expirydate.year)
#         #fine calculation
#         days=(date.today()-ib.issuedate)
#         print(date.today())
#         d=days.days
#         fine=0
#         if d>15:
#             day=d-15
#             fine=day*10
#
#
#         books=list(models.Book.objects.filter(isbn=ib.isbn))
#         students=list(models.StudentExtra.objects.filter(enrollment=ib.enrollment))
#         i=0
#         for l in books:
#             t=(students[i].get_name,students[i].enrollment,books[i].name,books[i].author,issdate,expdate,fine)
#             i=i+1
#             li.append(t)
#
#     return render(request,'library/viewissuedbook.html',{'li':li})


def viewissuedbook_view(request):
    issued_book_details = []

    for issued_book in IssuedBook.objects.all():
        # Convert date objects to formatted strings
        issued_date = issued_book.issuedate.strftime('%d-%m-%Y')
        expiry_date = issued_book.expirydate.strftime('%d-%m-%Y')
        # Calculate fine if applicable
        days_overdue = (date.today() - issued_book.issuedate).days
        fine = max(0, (days_overdue - 15) * 10)

        issued_book_details.append({
            'student_name': issued_book.student.first_name + ' ' + issued_book.student.last_name,
            'book_name': issued_book.book.bookname,
            'author': issued_book.book.author,
            'issued_date': issued_date,
            'expiry_date': expiry_date,
            'fine': fine,
            'id': issued_book.book.id,
        })

    return render(request, 'viewissuedbook.html', {'issued_book_details': issued_book_details})


def viewstudent_view(request):
    students = User.objects.filter(is_staff=False, is_superuser=False)
    return render(request, 'viewstudent.html', {'students': students})


def search_view(request):
    form = SearchForm(request.GET)
    results = []

    if form.is_valid():
        search_query = form.cleaned_data['search_query']
        results = Newbookmodel.objects.filter(name__icontains=search_query)  # Adjust based on your model fields

    return render(request, 'search_results.html', {'form': form, 'results': results})


def logout_user(request):
    # Clear the session variable storing the user's login state
    logout(request)
    return redirect('/')


def delete_book(request, book_id):
    # Retrieve the book object
    try:
        book = Newbookmodel.objects.get(id=book_id)
    except Newbookmodel.DoesNotExist:
        messages.error(request, 'Book not found.')
        return redirect('viewbook')  # Redirect to the book list page

    # Delete the book
    book.delete()
    messages.success(request, 'Book deleted successfully.')
    return redirect('viewbook')


def return_book(request, firstname, lastname):
    # Retrieve the book object
    try:
        book = IssuedBook.objects.get(firstname=firstname, lastname=lastname)
    except IssuedBook.DoesNotExist:
        messages.error(request, 'Book not found.')
        return redirect('viewissuedbook')  # Redirect to the book list page

    # Delete the book
    book.delete()
    messages.success(request, 'Book returned successfully.')
    return redirect('viewissuedbook')


def studentafterlogin(request):
    return render(request, 'studentafterlogin.html')


def viewissuedbookbystudent(request, stud_id):
    issued_book_details = IssuedBook.objects.filter(student=stud_id)
    issued_book_detail = []
    for i in issued_book_details:
        days_overdue = (date.today() - i.issuedate).days
        fine = max(0, (days_overdue - 15) * 10)
        issued_book_detail = fine
    print(issued_book_detail)
    return render(request, 'viewissuedbookbystudent.html', {'issued_book_details': issued_book_details,
                                                            'issued_book_detail': issued_book_detail})


def search_query(request):
    query = request.GET.get('search_query')
    results = None
    if query:
        results = Newbookmodel.objects.filter(bookname__icontains=query)
    return render(request, 'search_results.html', {'results': results, 'query': query})


def forgot_password(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        cpassword = request.POST.get('cpassword')
        if password == cpassword:
            user = User.objects.get(username=username)
            user.set_password(password)
            user.save()
            if user.is_staff == True:
                return redirect(adminsignin)
            elif user.is_staff == False:
                return redirect(studentlogin)
        else:
            msg = "Passsword didn't match. Try again!"
            return render(request, 'forgot_password.html', {'msg': msg})
    return render(request, 'forgot_password.html')


def studentafterlogin(request):
    return render(request, 'studentafterlogin.html')


from django.shortcuts import render, redirect, get_object_or_404
from .models import Newbookmodel


def editbook(request, book_id):
    book = get_object_or_404(Newbookmodel, id=book_id)

    if request.method == "POST":
        # Retrieve form data
        bookname = request.POST.get('bookname')
        author = request.POST.get('author')
        bookyear = request.POST.get('year')
        category = request.POST.get('category')
        desc = request.POST.get('desc')
        year = request.POST.get('year')
        shelfid = request.POST.get('shelfid')
        publisher = request.POST.get('publisher')

        # Check if bookname is provided
        if bookname:
            # Update book details
            book.bookname = bookname
            book.author = author
            book.bookyear = bookyear
            book.category = category
            book.year = year

            # Check if there's a new image, otherwise keep the old one
            if request.FILES.get('image'):
                book.image = request.FILES['image']

            book.desc = desc
            book.shelfid = shelfid
            book.publisher = publisher

            # Save the updated book object
            book.save()

            # Redirect to viewbook page or any other page you desire
            return redirect('viewbook')
        else:
            # If bookname is not provided, render the editbook form again with an error message
            return render(request, 'editbook.html', {'book': book, 'error_message': 'Book name is required'})

    # If it's a GET request, render the editbook form
    return render(request, 'editbook.html', {'book': book})
