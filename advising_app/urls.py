from django.urls import path

from . import views
from .views import delete_report

app_name = 'advising_app'
urlpatterns = [
    path('', views.index, name='index'),        #the base page is index.html
    path('report', views.renderReportForm, name='report'),
    path('submitReport', views.submitReport, name='submitReport'),
    path('logout', views.logout_prompt, name='logout_prompt'),
    path('perform_logout', views.perform_logout, name='perform_logout'),
    #path('about/', views.about, name='about'),
    path('about', views.about, name='about'),

    path('us', views.us, name='us'),
    path('view_report_user/<int:report_id>', views.view_report_user, name='view_report_user'),
    path('edit_report_admin/<int:report_id>', views.edit_report_admin, name='edit_report_admin'),
    path('report/delete/<int:report_id>/', delete_report, name='delete_report'),
]