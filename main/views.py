from django.shortcuts import  render, redirect
from .forms import NewUserForm,PostForm
from django.contrib.auth import login
from django.contrib import messages
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import AuthenticationForm 
from .models import Post
from django.views.generic import UpdateView,DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy


def IndexView(request):
    return render(request, 'index.html')

def register_request(request):
	if request.method == "POST":
		form = NewUserForm(request.POST)
		if form.is_valid():
			user = form.save()
			login(request, user)
			messages.success(request, "Roʻyxatdan muvaffaqiyatli o'tildi" )
			return redirect("home")
		messages.error(request, "Ro'yxatdan o'tishda xatolik.parolyoki usernameni qayta tekshirib ko'ring !")
	form = NewUserForm()
	return render (request=request, template_name="register.html", context={"register_form":form})

def login_request(request):
	if request.method == "POST":
		form = AuthenticationForm(request, data=request.POST)
		if form.is_valid():
			username = form.cleaned_data.get('username')
			password = form.cleaned_data.get('password')
			user = authenticate(username=username, password=password)
			if user is not None:
				login(request, user)
				messages.info(request, f"Siz hozir tizimga kirgansiz {username}.")
				return redirect("home")
			else:
				messages.error(request,"Foydalanuvchi nomi yoki parol noto‘g‘ri.")
		else:
			messages.error(request,"Foydalanuvchi nomi yoki parol noto‘g‘ri.")
	form = AuthenticationForm()
	return render(request=request, template_name="login.html", context={"login_form":form})

def PostAddView(request):
    if request.method == 'POST':
            form = PostForm(request.POST)
            if form.is_valid():
                form.save()
            return redirect('post')
    form = PostForm()
    context = {
        'forms': form
    }
        
    return render(request, 'postadd.html', context)

def PostView(request):
    Posts = Post.objects.all()
    return render(request, 'post.html', {'posts':Posts})

class Postupdateview(LoginRequiredMixin,UpdateView):
    model = Post
    template_name = 'post_update.html'
    fields = ('title','content','author')
    raise_exception=True

class Postdelateview(LoginRequiredMixin,DeleteView):
    model = Post
    template_name = 'post_delate.html'
    success_url = reverse_lazy('home')
    raise_exception=True
