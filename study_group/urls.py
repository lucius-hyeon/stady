from django.urls import path
from . import views
from . import recommend

app_name = 'studies'

urlpatterns = [
    path('', views.StudyListAPIView.as_view(), name='list'),
    path('<int:study_id>/', views.StudyDetailAPIView.as_view(),
         name='view_study'),  # 스터디 모집글 확인
    path('<int:study_id>/propose', views.StudyProposeView.as_view()),
    path('<int:study_id>/like', views.StudyLikeView.as_view()),
    path('<int:study_id>/accept/<int:user_id>/',
         views.StudentView.as_view(), name='accept'),
    path('search/', views.Search.as_view(), name='search'),
    path('recommand/', recommend.create_recommand_csv),
]
