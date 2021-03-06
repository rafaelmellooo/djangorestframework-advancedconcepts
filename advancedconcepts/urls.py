"""advancedconcepts URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from rest_framework import routers

from tourist_attractions.api.viewsets import TouristAttractionViewSet
from attractions.api.viewsets import AttractionViewSet
from business_hours.api.viewsets import BusinessHoursViewSet
from addresses.api.viewsets import AddressViewSet
from assessments.api.viewsets import AssessmentViewSet

router = routers.DefaultRouter()
router.register(r'tourist-attractions', TouristAttractionViewSet)
router.register(r'attractions', AttractionViewSet)
router.register(r'business-hours', BusinessHoursViewSet)
router.register(r'addresses', AddressViewSet)
router.register(r'assessments', AssessmentViewSet)

urlpatterns = [
    path('api/v1/', include(router.urls)),
    path('admin/', admin.site.urls),
]
