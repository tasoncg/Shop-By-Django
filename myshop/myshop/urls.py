"""myshop URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""

from django.conf.urls import url
from django.conf.urls.static import static
from django.contrib import admin
from django.conf import settings
from accounts import views as accounts_views
from django.contrib.auth import views as auth_views
from shop import views
urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$',views.home,name='home'),
    url(r'^buy/(?P<pk>\d+)/$',views.buy,name='buy'),
    url(r'^login/$', auth_views.LoginView.as_view(template_name='login.html'), name='login'),
    url(r'^logout/$',auth_views.LogoutView.as_view(), name='logout'),
    url(r'^signup/$',accounts_views.signup, name='signup'),
    url(r'^orders/$',views.orders,name='orders'),
    url(r'^order/(?P<pk>\d+)/$',views.order_detail,name='order_detail'),
    url(r'^checked_orders/$',views.checked_orders,name='checked_orders'),
    url(r'^checked_order/(?P<pk>\d+)/$',views.checked_order_detail,name='checked_order_detail'),
    url(r'^add_items/$',views.add_items,name='add_items'),
    # url(r'^account/(?P<pk>\d+)/$',views.acount, name='account')
]
if settings.DEBUG:
	urlpatterns+=static(settings.STATIC_URL,document_root=settings.STATIC_ROOT)
	urlpatterns+= static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
