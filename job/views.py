from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator
from .models import Job
from company.models import Company

@login_required
def create_job(request):
    """
    View for creating a job post. If the current user does not have a company profile,
    they are redirected to the company registration page. If the request method is POST,
    the job post is created with the provided data and the user is redirected to the job list page.
    Otherwise, the job creation form is rendered.
    """
    company = Company.objects.filter(user=request.user).first()
    if not company:
        return redirect('register_company')

    if request.method == 'POST':
        title = request.POST.get('title')
        description = request.POST.get('description')
        location = request.POST.get('location')
        salary_range = request.POST.get('salary_range')
        tags = request.POST.get('tags')

        Job.objects.create(
            company=company,
            title=title,
            description=description,
            location=location,
            salary_range=salary_range,
            tags=tags
        )

        return redirect('list_jobs')

    return render(request, 'job/create.html')


@login_required
def list_jobs(request):
    """ View for listing all job posts for the current user's company. """
    company = Company.objects.filter(user=request.user).first()
    if not company:
        return redirect('register_company')

   
    jobs = Job.objects.filter(company=company)

    paginator = Paginator(jobs, 2)
    page_number = request.GET.get('page')
    job_page = paginator.get_page(page_number)
    total_pages = job_page.paginator.num_pages

  
    return render(request, 'job/list.html', {
        'jobs': job_page,
        'total_pages': list(range(1, total_pages + 1))
    })


@login_required
def edit_job(request, job_id):
    """ View for editing a job post. If the request method is POST, the job post is updated with the new data. """
    job = get_object_or_404(Job, id=job_id, company__user=request.user)

    if request.method == 'POST':
    
        job.title = request.POST.get('title')
        job.description = request.POST.get('description')
        job.location = request.POST.get('location')
        job.salary_range = request.POST.get('salary_range')
        job.tags = request.POST.get('tags')
        job.save()

   
        return redirect('list_jobs')

 
    return render(request, 'job/edit.html', {'job': job})


@login_required
def delete_job(request, job_id):
    """ View for deleting a job post. If the request method is POST, the job post is deleted. """
    job = get_object_or_404(Job, id=job_id, company__user=request.user)

    if request.method == 'POST':
 
        job.delete()

        return redirect('list_jobs')

    return render(request, 'job/delete.html', {'job': job})
