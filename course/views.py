from django.shortcuts import redirect, render
from .models import User, Course
from .forms import RegisterForm, LoginForm
from .decorators import user_login_required

# Create your views here.
def get_user(request):
    return User.objects.get(id=request.session['user_id'])

@user_login_required
def index(request):
    if "user_id" in request.session:
        user = get_user(request)
        return render(request, "index.html",{"user":user})
    return render(request, "index.html")

def sign_up(request):
    form = RegisterForm()
    if request.method == "POST":
        username = request.POST['username']
        email = request.POST['email']
        if User.objects.filter(username=username).exists():
            error = "This username is already taken"
            return render(request,"sign-up.html",{"form":form, "error":error})
        if User.objects.filter(email=email).exists():
            error = "This email is already taken"
            return render(request,"sign-up.html",{"form":form, "error":error})
        form = RegisterForm(request.POST)
        new_user = form.save(commit=False)
        new_user.save()
        return redirect("login")
    return render(request, "sign-up.html",{"form":form})

def login_(request):
    form = LoginForm()
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        if User.objects.filter(username=username,password=password).exists():
            user = User.objects.get(username=username)
            request.session['user_id'] = user.id
            return redirect("index")
    return render(request, "login.html",{"form":form})

def logout_(request):
    if "user_id" in request.session:
        del request.session["user_id"]
    return redirect("login")

@user_login_required
def courses(request):
    courses = "python"
    return render(request, "courses.html",{"courses":courses})

@user_login_required
def course(request, course):
    if "user_id" in request.session:
        user = get_user(request)
        user.course_set.create(courses_name=course, no_of_users=0)
        return render(request, "course.html", {"course_name": course})

@user_login_required
def view_courses(request):
    if "user_id" in request.session:
        user = get_user(request)
        courses = user.course_set.all()
        return render(request,"view_courses.html", {"courses":courses})

def tutorial(request,course):
    return render(request,"tutorial.html",{"name":course})