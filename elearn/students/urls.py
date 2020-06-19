from students import views as students_views
from django.urls import path
from django.contrib.auth import views as auth_views

urlpatterns = [
	path('login/', auth_views.LoginView.as_view(template_name='students/student/login.html'), name = 'login'),
	path('logout/', auth_views.LogoutView.as_view(template_name='students/student/logout.html'), name = 'logout'),
	path('register/',students_views.StudentRegistrationView.as_view(), name='student_registration'),
	path('enroll-course/',students_views.StudentEnrollCourseView.as_view(), name='student_enroll_course'),
	path('courses/', students_views.StudentCourseListView.as_view(), name='student_course_list'),
	path('course/<pk>/', students_views.StudentCourseDetailView.as_view(), name='student_course_detail'),
	path('course/<pk>/<module_id>/', students_views.StudentCourseDetailView.as_view(), name='student_course_detail_module'),
]