from django.urls import path,include
from . import views

from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('',views.StudentAPIView)



urlpatterns = [
    # path('', views.student_list_view),
    # path('<int:pk>/',views.student_detailed_view),
    # path('', views.StudentListView.as_view()),
    # path('<int:pk>/',views.StudentDetailedView.as_view()),
    path('',include(router.urls))
]
