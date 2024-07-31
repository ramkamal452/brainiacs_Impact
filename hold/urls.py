from django.urls import path
from . import views
from django.conf import settings  
from django.conf.urls.static import static
import os
urlpatterns = [
    path('', views.run, name="login"),
    path('admin_page.html', views.admin_page, name='admin_page'),
    path('add.html', views.add, name='add'),
    path('addUser', views.addUser, name='addUser'),
    path('view.html', views.view, name='view'),
    path('viewUser', views.viewUser, name='viewUser'),
    path('delete.html', views.delete, name='delete'),
    path('deleteUser', views.deleteUser, name='deleteUser'),
    path('edit.html', views.edit, name="edit"),
    path('editUser', views.editUser, name="editUser"),
    path('delete_Q.html', views.delete_Q, name='delete_Q'),
    path('delete_Queue', views.delete_Queue, name='delete_Queue'),
    path('login.html', views.loginUser, name='loginUser'),
    path('studentData', views.studentData, name='studentData'),
    path('deptupdate', views.deptupdate, name='deptupdate'),
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=os.path.join(settings.BASE_DIR, 'static'))
   