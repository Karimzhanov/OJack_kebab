from django.urls import path
from apps.secondary import views

urlpatterns = [
    path('page_not_found/', views.page_not_found, name = 'page_not_found'),
    path('blog/', views.blog, name = 'blog'),
    path('blog-detail/<int:id>/', views.blog_detail, name = 'blog_detail'),
    path('cart/', views.cart, name = 'cart'),
    path('checkout/', views.checkout, name = 'checkout'),
    path('team/', views.team, name = 'team'),
    path('team-detail/', views.team_detail, name = 'team_detail'),
    path('gallery/', views.gallery, name = 'gallery'),
    path('menu/', views.menu, name = 'menu'),
    path('menu-detail/', views.menu_detail, name = 'menu_detail'),
]
