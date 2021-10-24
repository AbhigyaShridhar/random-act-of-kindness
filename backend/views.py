from django.shortcuts import render, redirect, get_object_or_404, HttpResponse, HttpResponseRedirect
from django.urls import reverse_lazy, reverse
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views import View
from .models import Queue, State, ContactUs, Item, Campaign, Organisation, User, Category, Ruby
from django.contrib.auth import login, logout, authenticate

# Create your views here.
def index(request):
    return render(request, 'backend/index.html')

def stream_file(request, pk):
    instance = get_object_or_404(Campaign, id=pk)
    response = HttpResponse()
    response['Content-Type'] = instance.content_type
    response['Content-Length'] = len(instance.picture)
    response.write(instance.picture)
    return response

def profile(request, pk):
    user = User.objects.get(id=pk)
    return render(request, "backend/profile.html", {
        "user": user,
    })

class Register(View):
    template = 'backend/register.html'
    success_url = 'backend:profile'

    def get(self, request):
        return render(request, self.template)

    def post(self, request):
        first_name = request.POST["first_name"]
        last_name = request.POST["last_name"]
        contact = request.POST["contact"]
        email = request.POST["email"]
        p1 = request.POST["p1"]
        p2 = request.POST["p2"]

        if not p1 == p2:
            return render(request, self.template, {
                'message': "passwords don't match",
            })

        if not p1 or not p2 or not first_name or not last_name or not contact or not email:
            return render(request, self.template, {
                'message': "Please enter all fields",
            })

        try:
            user = User.objects.create(first_name=first_name, last_name=last_name, email=email, username=email, password=p1)
            user.save()
        except:
            return render(request, self.template, {
                'message': "User with these credentials already exists",
            })
        login(request, user)

        return HttpResponseRedirect(reverse(self.success_url, kwargs={'pk':user.id, }))

class Login(View):
    template = 'backend/login.html'
    success_url = 'backend:index'

    def get(self, request):
        return render(request, self.template)

    def post(self, request):
        username = request.POST['username']
        password = request.POST['password']

        if not username or not password:
            return render(request, self.template, {
                'message': "Please enter all fields",
            })

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
        else:
            return render(request, self.template, {
                "message": "Invalid username and/or password."
            })

        return HttpResponseRedirect(reverse(self.success_url))

def logout_view(request):
    logout(request)
    return HttpResponseRedirect(reverse("backend:index"))

def faq(request):
    return render(request, "backend/faq.html")

class Contact(View):
    template = 'backend/contact-us.html'

    def get(self, request):
        return render(request, self.template)

    def post(self, request):
        From = request.POST['name']
        message = request.POST['message']
        email = request.POST['email']
        subject = request.POST['subject']

        instance = ContactUs.objects.create(From=From, message=message, email=email, subject=subject)
        instance.save()

        return render(request, self.template, {
            "message": "Thank You, we got your message and will get back to you."
        })

def checkout(request, num):
    return render(request, "backend/checkout.html", {
        'num': num,
        'total': 5 * num,
    })

class Rubies(View):
    template = "backend/buy_rubies.html"
    success_url = "backend:checkout"

    def get(self, request):
        if not request.user.is_authenticated:
            return HttpResponseRedirect(reverse("backend:registration"))
        return render(request, self.template)

    def post(self, request):
        num = request.POST['num']
        return HttpResponseRedirect(reverse(self.success_url, kwargs={'num':num, }))
