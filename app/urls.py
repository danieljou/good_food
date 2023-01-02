from django.urls import path 
from .views import *
urlpatterns = [
    path("", index, name="home"),
    path("redirect_user/", redirect_user, name="redirect_user"),
    path("admin_dash/", admin_dash, name="admin_dash"),
    path("user_dash/", user_dash, name="user_dash"),
    path("delete_repas/<id>", delete_repas, name="delete_repas"),
    path("update_repas/<id>", update_repas, name="update_repas"),
    path("create_repas/", create_repas, name="create_repas"),
    path("create_account/", create_account, name="create_account"),

    # Menu Management routes
    path("menu/", menu, name="menu"),
    path("create_menu/", create_menu, name="create_menu"),
    path("update_menu/<id>", update_menu, name="update_menu"),
    path("delete_menu/<id>", delete_menu, name="delete_menu"),

]
