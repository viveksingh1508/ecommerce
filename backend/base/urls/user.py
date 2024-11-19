from django.urls import path
from base.views import users


urlpatterns = [
    path("login/", users.MyTokenObtainPairView.as_view(), name="token_obtain_pair"),
    path("profile/", users.getUserProfile, name="users-profile"),
    path("", users.getUsers, name="users"),
    path("register", users.registerUser, name="register"),
]
