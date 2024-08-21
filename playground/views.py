from django.shortcuts import render
from django.http import HttpResponse
from django.urls import reverse_lazy
from .models import Product
from django.views.generic import  CreateView,     DetailView,     ListView,     DeleteView,     ListView,     UpdateView
from django.shortcuts import render, get_object_or_404 
# Create your views here.
# viwes have a function that takes request and return response
# request handler 
 
class Product_list_view(ListView):
    model = Product  
    template_name = "hello.html"
    def list_obj(self):
        return Product.objects.all()
       

# FBV 
def product_detail(request, pk):
    product = get_object_or_404(Product, pk=pk)
    context = {
        "product": product.title
    }
    return render(request,"home.html",context)

# CBV
class products_detail(DetailView):
    model = Product
    template_name = "home.html"
    def get_obj(self):
        return super().get_object()



# def say_hello(request):
#     my_context = {
#         "name":"israel",
#         "age":23,
#         "skils":["nodeJs","Django", "python", "javascript"]
#     }
#     return render(request, 'hello.html', my_context)





# def home(request):
#     return render(request, 'home.html')

# def about(request):
#     return render(request, 'about.html')


# def create_product(request):
#     obj = Product.objects.get(id=1)
#     # return obj.title
#     my_obj = {
#         "object":obj
#     }
#     return render(request, "home.html",my_obj ) 


# def create_form(request):
#     form = ProductForm(request.POST or None)
#     if form.is_valid():
#         form.save()
#         form = ProductForm()
#     my_form = {
#         "form": form
#     }
#     return render(request, "home.html",my_form)

# def standarf_form(request):
#     s_form = django_standard_form(request.POST)
#     context = {
#         "form":s_form
#     }
#     return render(request, "hello.html", context)


# def product_view(ListView):
#     queryset = Product.objects.all()