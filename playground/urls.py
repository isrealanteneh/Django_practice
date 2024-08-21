from django.urls import path, include
from . import views


# urlconfig
urlpatterns = [
    path("", views.Product_list_view.as_view(), name="product_list"),
    path("<int:pk>/", views.products_detail.as_view(), name="product_detail"),
    # path('',product_view.as_view(), name="articleview")
    # path("hello/", views.say_hello ),
    # path("home/", views.home ),
    # path("about/", views.about ),
    # path("order/",views.create_product)
    # path('',views.product_view, name='pro_view'),
    # path("form/", views.create_form),
    # path("newform/", views.standarf_form)
]