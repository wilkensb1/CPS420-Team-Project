from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.views.generic import ListView, DetailView, CreateView
from django.urls import reverse_lazy
from .models import Job, JobCategory, UserProfile, Application
from .forms import ApplicationForm

# Create your views here.
class JobListView(ListView):
    model = Job
    template_name = 'job_list.html'
    context_object_name = 'jobs'
    ordering = ['-published_date']

class JobDetailView(DetailView):
    model = Job
    template_name = 'job_detail.html'
    context_object_name = 'job'

@login_required
def apply_for_job(request, pk):
    job = get_object_or_404(Job, pk=pk)

    if request.method == 'POST':
        form = ApplicationForm(request.POST, request.FILES)
        if form.is_valid():
            application = form.save(commit=False)
            application.job = job
            application.applicant = request.user
            application.save()
            return redirect('job_detail', pk=pk)
    else:
        form = ApplicationForm()

    return render(request, 'apply_for_job.html', {'form': form, 'job': job})

class UserProfileView(DetailView):
    model = UserProfile
    template_name = 'user_profile.html'
    context_object_name = 'user_profile'
    slug_field = 'user__username'
    slug_url_kwarg = 'username'

class JobCategoryListView(ListView):
    model = JobCategory
    template_name = 'job_category_list.html'
    context_object_name = 'job_categories'

class JobCategoryDetailView(DetailView):
    model = JobCategory
    template_name = 'job_category_detail.html'
    context_object_name = 'job_category'