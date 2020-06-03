
from rest_framework.authtoken import views
from rest_framework.routers import DefaultRouter

from django.urls import path

from .apiviews import PollViewSet, ChoiceList, CreateVote, UserCreate
from .views import polls_list

router = DefaultRouter()
router.register('polls', PollViewSet, basename='polls')

urlpatterns = [
    path("polls/<int:pk>/choices/", ChoiceList.as_view(), name="choice-list"),
    path("polls/<int:pk>/choices/<int:choice_pk>/vote/", CreateVote.as_view(), name="create-vote"),
    path("users/", UserCreate.as_view(), name="user_create"),
    # path("login/", LoginView.as_view(), name="login")
    path("login/", views.obtain_auth_token, name="login"),
]

urlpatterns += router.urls