"""elearn URL Configuration

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

from django.contrib.auth.decorators import login_required, permission_required
from django.contrib import admin
from django.urls import path, include
from django.contrib.auth import views as auth_views
from educa import views as educa_views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('courses/', login_required(educa_views.CourseListView.as_view()), name='course_list'),
    path('admin/', admin.site.urls),
    path('my_courses/', educa_views.ManageCourseListView.as_view(),name='manage_course_list'),
	path('create/', educa_views.CourseCreateView.as_view(), name='course_create'),
	path('<pk>/edit/', educa_views.CourseUpdateView.as_view(), name='course_edit'),
	path('<pk>/delete/', educa_views.CourseDeleteView.as_view(), name='course_delete'),
    path('<pk>/module/', educa_views.CourseModuleUpdateView.as_view(), name='course_module_update'),
    path('content/<id>/delete/',educa_views.ContentDeleteView.as_view(), name='module_content_delete'),
    path('module/<module_id>/', educa_views.ModuleContentListView.as_view(), name='module_content_list'),
    path('module/<module_id>/content/<model_name>/create/',educa_views.ContentCreateUpdateView.as_view(), name='module_content_create'),
    path('module/<module_id>/content/<model_name>/<id>/', educa_views.ContentCreateUpdateView.as_view(), name='module_content_update'),
    path('subject/<subject>/', educa_views.CourseListView.as_view(), name='course_list_subject'),
    path('<slug>/',educa_views.CourseDetailView.as_view(), name='course_detail'),
    path('student/', include('students.urls')),
    path('api/', include('educa.api.urls', namespace='api')),  
]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)