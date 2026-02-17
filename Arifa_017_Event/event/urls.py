from django.urls import path
from .views import *
urlpatterns = [
    path('home/', homePage, name="home" ),
    path('login', loginPage, name="login" ),
    path('', signupPage, name="signup" ),
    path('logout/', logoutPage, name="logout" ),
    path('changepassword/', changepassword, name="changepassword" ),

    path('categorylist/', categoryPage, name="category"),
    path('addcategory/', addcategoryPage, name="addcate"),
    path('editcategory/<int:id>/', editcategoryPage, name="editcate"),
    path('deletecategory/<int:id>/', deletecategoryPage, name="deletecate"),


    path('eventlist/', eventPage, name="event"),
    path('addevent/', addeventPage, name="addevent"),
    path('editevent/<int:id>/', editeventPage, name="editevent"),
    path('deleteevent/<int:id>/', deleteeventPage, name="deleteevent"),
    path('view/<int:id>/', ViewPage, name="view"),
    path('changestatus/<int:id>/', changestatus, name="changestatus"),
]