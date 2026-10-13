from django.contrib.auth.views import LoginView, LogoutView
from django.db.models import Q
from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from django.contrib.auth import login,logout
from django.template.defaultfilters import title
from django.template.defaulttags import comment
from django.urls import reverse, reverse_lazy
from django.views.generic import ListView, DetailView, CreateView

from blog.forms import SignUpFrom, SignInForm, CommentForm
from blog.models import Product, Comment


# def home(request):
#     products = Product.objects.all()
#     context = {
#         "products":products
#     }
#     return render(request,"blog/index.html",context)

# def signup(request):
#     if request.method == "POST":
#         form = SignUpFrom(data=request.POST)
#         if form.is_valid():
#             user = form.save()
#             return redirect("home")
#     else:
#         form = SignUpFrom()
#     context = {
#             "form": form
#     }
#     return render(request, "blog/signup.html", context)



# def signin(request):
#     if request.method == "POST":
#         form =SignInForm(data=request.POST)
#         if form.is_valid():
#             user = form.get_user()
#             login(request,user)
#             return redirect("home")
#     form = SignInForm()
#     context = {
#         "form":form
#     }
#     return render(request, "blog/signin.html", context)


# def signout(request):
#     logout(request)
#     return redirect("signin")

# def detail(request, pk):
#     product = get_object_or_404(Product,pk=pk)
#     comment = Comment.objects.filter(article=product)
#     return render(request, "blog/detail.html", {"product":product , "comment_form":CommentForm(),"comments":comment})

# def category(request,pk):
#     product = Product.objects.filter(category_id=pk)
#     context = {
#         "products":product
#     }
#     return render(request, "blog/category.html", context)

# def search(request):
#     word = request.GET.get("query")
#     products = Product.objects.filter(Q(title__icontains=word))
#     context = {
#         "products":products
#     }
#     return render(request, "blog/search.html", context)

# def add_comment(request,pk):
#     form = CommentForm(data=request.POST)
#     if form.is_valid():
#         comment = form.save(commit=False)
#         comment.user = request.user
#         comment.article = Product.objects.get(pk=pk)
#         comment.save()
#     else:
#         pass
#     return redirect("detail",pk)

class Home(ListView):
    model = Product
    template_name = "blog/index.html"
    context_object_name = "products"

class Category(Home):
    def get_queryset(self):
        return Product.objects.filter(category_id=self.kwargs['pk'])

class Search(Home):
    def get_queryset(self):
        word = self.request.GET.get("query")
        return Product.objects.filter(Q(title__icontains=word))

class Detail(DetailView):
    model = Product
    template_name = "blog/detail.html"
    context_object_name = "product"

    def get_context_data(self, **kwargs):
        context = super().get_context_data()
        product = Product.objects.get(pk=self.kwargs['pk'])
        comments = Comment.objects.filter(article=product)
        context["comments"] = comments
        context["comment_form"] = CommentForm
        return context

class AddComment(CreateView):
    model = Comment
    form_class = CommentForm
    template_name = "blog/detail.html"
    def form_valid(self, form):
        form.instance.user = self.request.user
        form.instance.article = Product.objects.get(pk=self.kwargs['pk'])
        return super().form_valid(form)
    def get_success_url(self):
        return reverse("detail",kwargs={"pk":self.kwargs['pk']})

class SignUp(CreateView):
    form_class = SignUpFrom
    template_name = "blog/signup.html"
    success_url = reverse_lazy("home")

    def form_valid(self, form):
        user = form.save()
        return super().form_valid(form)

class SignIn(LoginView):
    template_name = "blog/signin.html"
    authentication_form = SignInForm
    def get_success_url(self):
        return reverse_lazy("home")

class SignOut(LogoutView):
    next_page = reverse_lazy("signin")

