from django import forms

from . models import IssuedBook,Newbookmodel,studentsignupmodel


# class IssuedBookForm(forms.ModelForm):
#     class Meta:
#         model = IssuedBook
#         fields = ['firstname', 'lastname', 'bookname', 'author']

#     def __init__(self, *args, **kwargs):
#         super().__init__(*args, **kwargs)
#         self.fields['firstname'].label = 'First Name'
#         self.fields['lastname'].label = 'Last Name'
#         self.fields['bookname'].label = 'Book Name'
#         self.fields['author'].label = 'Author'
#         self.fields['bookname'].queryset = Newbookmodel.objects.all()
#         self.fields['author'].queryset = Newbookmodel.objects.all()
#         self.fields['firstname'].queryset = studentsignupmodel.objects.all()
#         self.fields['lastname'].queryset = studentsignupmodel.objects.all()

class SearchForm(forms.Form):
    search_query = forms.CharField(max_length=255, required=False, label='Search')