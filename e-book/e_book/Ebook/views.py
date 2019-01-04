from django.shortcuts import render,redirect
from django.views.generic import TemplateView
from .models import User, Books, User_Book
from django.core.files.storage import FileSystemStorage

# Create your views here.

class HomePage(TemplateView):
    def get(self,request):
        book = Books.objects.filter(public=True).values()
        return render(request, "index.html",context={'books': list(book)})
    def signup(request):
        return render(request, "signup.html", context={})
    def register_user(request):
        details = request.POST
        data = User(name=details.get('user_name'),user_id=details.get('user_id'),password=details.get('user_pass'))
        data.save()
        return render(request, "signin.html", context={})
    def signin(request):
        return render(request, "signin.html", context={})
    def login(request):
        details = request.POST
        exist = User.objects.filter(user_id=details.get("user_id"),password=details.get("user_pass")).exists()
        if exist:
            request.session['user_id'] = details.get("user_id")
            book = User_Book.objects.select_related('book').filter(user_id_id=details.get("user_id")).values('book')
            book_d = Books.objects.filter(id__in=book).values()
            return render(request, "dashboard.html", context={'books':book_d})
        else:
            return render(request, "signin.html", context={})
def upload(request):
    if request.method == "POST":
        upload_file = request.FILES['document']
        req = request.POST
        public = False
        if "book_public_true" in req:
            public = True
        book = Books(name=req.get("book_name"),category=req.get("book_cat"),author_name=req.get("book_auth_name"),no_of_pages=req.get("book_no_of_pages"),tags=req.get("book_tags"),public=public,filename=upload_file.name)
        book.save()
        user_id = request.session['user_id']
        user = User.objects.get(user_id=user_id)
        user_book = User_Book(user_id=user,book=book)
        user_book.save()
        fs = FileSystemStorage()
        fs.save(upload_file.name,upload_file)

    book = User_Book.objects.select_related('book').filter(user_id_id=user_id).values('book')
    book_d = Books.objects.filter(id__in=book).values()
    return render(request, "dashboard.html", context={'books': book_d})

