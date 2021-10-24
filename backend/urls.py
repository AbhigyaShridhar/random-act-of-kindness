from django.urls import path

from . import views

app_name = 'backend'

urlpatterns = [
    path('', views.index, name='index'),
    path('faqs', views.faq, name='faq'),
    path('contact-us', views.Contact.as_view(), name='contact'),
    path('accounts/register', views.Register.as_view(), name='registration'),
    path('accounts/login', views.Login.as_view(), name='login'),
    path('accounts/logout', views.index, name='logout'),
    path('rubies/donate', views.Rubies.as_view(), name='donate'),
    path('profile/<str:pk>', views.profile, name='profile'),
    path('active/campaigns', views.index, name='campaigns'),
    path('profile/update', views.index, name='update_profile'),
]
