from django.shortcuts import render
from .models import Courses, Lecturers
from django.db.utils import IntegrityError

# Create your views here.


def index(request):
    user = request.session["user"] = "guest"
    return render(request, "index.html", {"user": user})

###


def add_course(request):
    message = ""
    all_lecturers = Lecturers.objects.all()

    try:
        if request.method == 'POST':
            name = request.POST["course"]
            lecturer = request.POST["lecturer"]
            description = request.POST["description"]
            course = Courses(
                name=name, lecturer=lecturer, description=description)
            course.save()
            message = f"{name} Added successfully"
            return render(request, "courses.html", {"message": message})
        elif request.method == 'GET':
            return render(
                request, "courses.html", {"all_lecturers": all_lecturers})
    except IntegrityError:
        message = (f"{name} Already exists")
        return render(request, "courses.html", {"message": message})


def search_course(request):
    search_results_name = []
    if request.method == 'POST':
        search = request.POST["search"]
        all_courses = Courses.objects.all()
        for r in all_courses:
            if r.name == search:
                search_results_name.append(r)
    return render(
        request, "search_courses.html", {"search_name": search_results_name})


def see_all_courses(request):
    all_courses = Courses.objects.all()
    return render(request, "all_courses.html", {"all_courses": all_courses})

###


def add_lecturer(request):
    message = ""
    try:
        if request.method == 'POST':
            name = request.POST["name"]
            email = request.POST["email"]
            can_teach = request.POST["can_teach"]
            lecturer = Lecturers(name=name, email=email, can_teach=can_teach)
            lecturer.save()
            message = f"{name} Added successfully"
        return render(request, "lecturers.html", {"message": message})
    except IntegrityError:
        message = (f"{name} Already exists")
        return render(request, "lecturers.html", {"message": message})


def lecturers(request):
    all_lecturers = Lecturers.objects.all()
    return render(request, "lecturers.html", {"all_lecturers": all_lecturers})


###

def to_be_continued(request):
    return render(request, "to_be_continued.html")
