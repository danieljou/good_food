from django.urls import path 
from .views import *
urlpatterns = [
    path("", index, name="home"),
    path("redirect_user/", redirect_user, name="redirect_user"),
    path("admin_dash/", admin_dash, name="admin_dash"),
    path("user_dash/", user_dash, name="user_dash"),
    
    # Repas management
    path("delete_repas/<id>", delete_repas, name="delete_repas"),
    path("update_repas/<id>", update_repas, name="update_repas"),
    path("create_repas/", create_repas, name="create_repas"),
    path("create_account/", create_account, name="create_account"),
    path("commander_repas/<id>", commander_repas, name="commander_repas"),

    # Menu Management routes
    path("menu/", menu, name="menu"),
    path("create_menu/", create_menu, name="create_menu"),
    path("update_menu/<id>", update_menu, name="update_menu"),
    path("delete_menu/<id>", delete_menu, name="delete_menu"),
    path("commander_menu/<id>", commander_menu, name="commander_menu"),

    # Command Management 
    path("command_list/", command_list, name="command_list"),
    path("command_list_user/", command_list_user, name="command_list_user"),
    #
    path("menu_page/", menu_page, name="menu_page"),
    path("menu_details/<id>", menu_details, name="menu_details"),    

    # 
    path("resrvation_list_user/", resrvation_list_user, name="resrvation_list_user"),

]
