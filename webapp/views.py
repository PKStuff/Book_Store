from django.shortcuts import render,redirect
from .models import Books, Review
from .forms import Books_Form, Register_form, email_form, Review_Form
from django.contrib.auth.views import login_required
from django.contrib.auth.admin import User
from django.contrib.auth import authenticate, login
import random
from django.core.mail import EmailMessage

user = None
def display(request):
    try:
        global user
        user = User.objects.get(username=request.user.username)
    except User.DoesNotExist:
        user = None
    form1 = Books.objects.all()
    most_rated_books = []
    for char in form1:
        total = Review.objects.filter(Book=char.id).count()
        review_sum = sum(Review.objects.filter(Book=char.id).values_list('rating',flat=True))
        if review_sum > 0 and (review_sum/total) > 1:
            most_rated_books.append(char.id)

    form = Books.objects.filter(pk__in=most_rated_books)
    names = set(Books.objects.all().values_list('related_to',flat=True))
    return render(request,'webapp/index.html',{'form':form,'user':user,'names':names,'most_rated_books':most_rated_books})

def display_review(request,book_id):
    try:
        reviews = Review.objects.filter(Book=book_id).order_by('-rating')
        book = Books.objects.filter(pk=book_id)
    except Review.DoesNotExist:
        reviews = 'Reviews Not Found'

    return render(request,'webapp/review_display.html',{'reviews':reviews,'book_id':book_id,'user':user,'book':book})

@login_required
def upload_file(request):

    if request.method == 'POST':
        form = Books_Form(request.POST, request.FILES)
        form.instance.user = request.user
        if form.is_valid():
            form = form.save(commit=False)
            form.save()

            return redirect('index')
    else:
        form = Books_Form()
    return render(request, 'webapp/upload_file.html',{'form':form})

def email_validate(request):

    if request.method == 'POST':
        form = Register_form(request.POST)
        if form.is_valid():
            fs = form.save(commit=False)
            fs.set_password(fs.password)
            fs.save()

            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')

            user = authenticate(username=username, password=password)

            if user:
                login(request,user)
                return redirect('index')
    else:
        form = Register_form()
    return render(request,'webapp/register.html',{'form':form})

def email_send(request):

    if request.method == 'POST':
        form = email_form(request.POST)
        if form.is_valid():
            form.save(commit=False)
            email_address = form.cleaned_data.get('username')
            print(email_address)
            otp = random.randrange(1000000000,9999999999)
            print(otp)
            email = EmailMessage('One Time Password', otp, to=[email_address])
            email.send()
            return redirect('register')
    else:
        form = email_form()
    return render(request,'webapp/email.html',{'form':form})

@login_required
def write_review(request,book_id):
    error = None
    userobj = Review.objects.filter(Book=book_id).values('user')
    userdata = User.objects.filter(pk__in=userobj).values_list('username',flat=True)
    if request.user.username not in userdata:
        if request.method == 'POST':
            form = Review_Form(request.POST)

            form.instance.user = request.user
            if form.is_valid():
                form = form.save(commit=False)
                book = Books.objects.get(pk=book_id)
                form.Book = book
                form.save()
                return redirect('index')
        else:
            form = Review_Form()
        return render(request, 'webapp/review.html', {'form': form})
    else:
        error = 'You already recorded your response'
        return render(request, 'webapp/review.html', {'error': error,'book_id':book_id})


def bookgroup(request,book_grp_name):
    error_msg = None
    try:
        form = Books.objects.filter(related_to=book_grp_name)
    except Books.DoesNotExists:
        error_msg = "Books not available"
    names = set(Books.objects.all().values_list('related_to', flat=True))
    return render(request,'webapp/books.html',{'form':form,'error_msg':error_msg,'names':names})