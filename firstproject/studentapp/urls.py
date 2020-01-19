from django.urls import path
from . import views

urlpatterns = [
    # path('', views.student_list_view),
    # path('<int:pk>/',views.student_detailed_view),
    path('', views.StudentListView.as_view()),
    path('<int:pk>/',views.StudentDetailedView.as_view())
]
