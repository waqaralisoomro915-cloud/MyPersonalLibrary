from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import redirect
from .models import Contact, requestbook,favourite_books_update,ArivalBooks


# home function
def home(request):
    return render(request,'home.html')


# about page
def about(request):
    return render(request,'about.html')

#contact page
from django.shortcuts import render
from .models import Contact

def contact(request):
    if request.method == 'POST':
        print("POST data received:", request.POST)  # debug line
        firstname = request.POST.get('firstName')
        lastname = request.POST.get('lastName')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        subject = request.POST.get('subject')
        message = request.POST.get('message')

        contactform = Contact(
            firstname=firstname,
            lastname=lastname,
            email=email,
            phone=phone,
            subject=subject,
            message=message,

        )
        contactform.save()
    return render(request, 'contact.html')


#books page
def books(request):
    return render(request,'books.html')


#categories page
def categories(request):
    return render(request,'categories.html')




# favourite page
def favourites(request):
    favourite_books=favourite_books_update.objects.all()
    return render(request,'favourite.html',{"favourite_books":favourite_books})

#arval page
def arivals(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        author = request.POST.get('author')
        ins=requestbook(
            title=title,
            author=author,

        )
        ins.save()
    new_books=ArivalBooks.objects.all()
    return render(request,'arivals.html',{'new_books':new_books})



def privacy(request):
    return render(request,'privacypolicy.html')
