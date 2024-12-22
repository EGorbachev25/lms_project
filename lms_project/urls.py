"""
URL configuration for lms_project project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
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
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from rest_framework.routers import DefaultRouter
from rest_framework import permissions

from courses.viewsets import CourseViewSet, ReviewViewSet
from lessons.viewsets import LessonViewSet, MaterialViewSet
from homework.viewsets import HomeworkViewSet, GradeViewSet
from orders.viewsets import OrderViewSet, PaymentViewSet
from forums.viewsets import ForumViewSet, TopicViewSet, CommentViewSet

router = DefaultRouter()

router.register(r'courses', CourseViewSet, basename='course')
router.register(r'courses/reviews', ReviewViewSet, basename='review')
router.register(r'lessons', LessonViewSet, basename='lesson')
router.register(r'lessons/materials', MaterialViewSet, basename='material')
router.register(r'homework', HomeworkViewSet, basename='homework')
router.register(r'homework/grades', GradeViewSet, basename='grade')
router.register(r'orders', OrderViewSet, basename='order')
router.register(r'orders/payments', PaymentViewSet, basename='payment')
router.register(r'forums', ForumViewSet, basename='forum')
router.register(r'forums/topics', TopicViewSet, basename='topic')
router.register(r'forums/comments', CommentViewSet, basename='comment')


schema_view = get_schema_view(
    openapi.Info(
        title="LMS API",
        default_version='v1',
        description="API documentation for LMS project",
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
]

