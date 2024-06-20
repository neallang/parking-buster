import os

from django.contrib import messages
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User, AnonymousUser
from advising_app.models import UserProfile

from django.http import HttpResponseRedirect, HttpResponseForbidden
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse

from .forms import ReportForm, AdminViewForm
from .models import Report

"""The index page is where users log in. If successful, 
    they are then passed to the user_home page, where their name
#    is displayed. To achieve this, we must pass the name to that
#    page, but ONLY if they are authenticated, as the name doesn't
#    exist if they aren't and will trigger an error."""


# def getMediaFileKeys(aws_access_key, aws_secret_key):
#     session = boto3.Session(aws_access_key_id=aws_access_key, aws_secret_access_key=aws_secret_key)
#     s3 = session.resource('s3')
#     media_bucket = s3.Bucket(AWS_STORAGE_BUCKET_NAME)
#
#     files = []
#
#     for object in media_bucket.objects.all():
#         if not object.key.startswith('admin/'):
#             #os.path.splitext splits into filename and extension
#             extension = os.path.splitext(object.key)[1]
#             files.append({
#                 'key': object.key,
#                 'url': f'https://{AWS_STORAGE_BUCKET_NAME}.s3.amazonaws.com/{object.key}',
#                 'extension': extension
#             })
#
#     return files


def index(request):
    if request.user.is_authenticated:
        first_name = request.user.first_name
        username = request.user.username
        #is_admin = request.user.profile.admin
        if request.user.profile.site_admin and not request.user.is_superuser: # Admin path
            # bucketKeys = getMediaFileKeys(AWS_ACCESS_KEY_ID, AWS_SECRET_ACCESS_KEY)
            reports = Report.objects.all().order_by('-created_at')
            new_reports = Report.objects.filter(status='New').order_by('-created_at')
            in_progress_reports = Report.objects.filter(status='In Progress').order_by('-created_at')
            resolved_reports = Report.objects.filter(status='Resolved').order_by('-created_at')
            return render(request, 'advising_app/admin_home.html',{
                'is_authenticated': True,
                'first_name': first_name,
                'username': username,
                # 'bucket_keys': bucketKeys,
                'reports': reports,
                'new_reports': new_reports,
                'in_progress_reports': in_progress_reports,
                'resolved_reports': resolved_reports
            })
        else:
            reports = Report.objects.filter(user_profile__user=request.user).order_by('-created_at')
            new_reports = Report.objects.filter(user_profile__user=request.user, status='New').order_by('-created_at')
            in_progress_reports = Report.objects.filter(user_profile__user=request.user, status='In Progress').order_by('-created_at')
            resolved_reports = Report.objects.filter(user_profile__user=request.user, status='Resolved').order_by('-created_at')
            #this works for a superuser only if the account is first made on the site
            #and then the admin settings are changed to include admin and superuser
            return render(request, 'advising_app/user_home.html', {
                'is_authenticated': True,
                'first_name': first_name,
                'username': username,
                'reports': reports,
                'new_reports': new_reports,
                'in_progress_reports': in_progress_reports,
                'resolved_reports': resolved_reports
            })
    else:
        return render(request, 'advising_app/index.html', {'is_authenticated': False})

def submitReport(request):
    if request.method == 'POST':
        form = ReportForm(request.POST, request.FILES)
        if form.is_valid():
            if request.user.is_authenticated:
                report = form.save(commit=False)
                # Directly get the authenticated user's UserProfile
                user_profile = request.user.profile
                redirect_url = reverse("advising_app:index")  # Redirect authenticated users here
                report.user_profile = user_profile
                report.save()
            else:
                report = form.save(commit=False)
                # Check if the user AnonymousUser is already in the database
                anonUserExists = False
                existingUsers = User.objects.all()
                for user in existingUsers:
                    if user.username == 'AnonymousUser':
                        anonUserExists = True
                        break
                
                anonymous_user = None
                anonymous_user_profile = None
                if (not anonUserExists):
                    anonymous_user = User.objects.create(username='AnonymousUser')
                    anonymous_user_profile = UserProfile.objects.create(user=anonymous_user)
                else:
                    anonymous_user = User.objects.filter(username='AnonymousUser')[0]
                    anonymous_user_profile = UserProfile.objects.filter(user=anonymous_user)[0]

                
                report.user_profile = anonymous_user_profile
                report.save()
                redirect_url = reverse("advising_app:index")  # Redirect anonymous users here
            return HttpResponseRedirect(redirect_url)
        else:
            form = ReportForm()
            return HttpResponseRedirect(reverse("advising_app:index"))

    return HttpResponseRedirect(reverse("advising_app:index"))

def renderReportForm(request):
    form = ReportForm(use_required_attribute=False)
    if request.user.is_authenticated:
        user_name = request.user.username
    else:
        user_name = "AnonymousUser"

    return render(request, "advising_app/reportForm.html", {'form': form, 'username': user_name})

def logout_prompt(request):
    # Simply renders the confirmation page
    return render(request, 'advising_app/logged_out.html')

def perform_logout(request):
    logout(request)
    return HttpResponseRedirect(reverse("advising_app:index"))

def about(request):
    return render(request, 'advising_app/about.html')
def us(request):
    return render(request, 'advising_app/us.html')

def view_report_user(request, report_id):
    report = get_object_or_404(Report, pk=report_id)
    if request.user.username != report.user_profile.user.username:
        return HttpResponseRedirect(reverse("advising_app:index"))
    # getMediaFileKeys(AWS_ACCESS_KEY_ID, AWS_SECRET_ACCESS_KEY)
    return render(request, 'advising_app/view_report_user.html', {'report': report})

def edit_report_admin(request, report_id):
    report = get_object_or_404(Report, pk=report_id)
    if report.status == "New":
        report.status = "In Progress"
        report.save()
    if request.method == "POST":
        form = AdminViewForm(request.POST, instance=report)
        if form.is_valid():
            form.save()
            messages.success(request, "Report updated successfully.")
            return HttpResponseRedirect(reverse("advising_app:index"))
    else:
        form = AdminViewForm(instance=report)

    return render(request, 'advising_app/edit_report_admin.html', {
        'form': form,
        'report': report
    })

@login_required
def delete_report(request, report_id):
    report = get_object_or_404(Report, id=report_id, user_profile__user=request.user)
    if request.method == 'POST':
        report.delete()
        return redirect('advising_app:index')
    else:
        return HttpResponseForbidden()

#omitted for privacy reasons. Amazon S3 account has been shut down since May 2024.
# AWS_ACCESS_KEY_ID = ''
# AWS_SECRET_ACCESS_KEY = ''
# AWS_STORAGE_BUCKET_NAME = '