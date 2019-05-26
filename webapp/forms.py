from django import forms
from .models import Books, Review
from django.contrib.auth.admin import User

class Books_Form(forms.ModelForm):

    class Meta:
        model = Books
        fields = ['book_name','author', 'publication', 'edition', 'more_info', 'file', 'front_page','related_to']


class Register_form(forms.ModelForm):

    password = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ['username', 'password']

class email_form(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username']


class Review_Form(forms.ModelForm):

    class Meta:
        model = Review
        fields = ['rating', 'review']