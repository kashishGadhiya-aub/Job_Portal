from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator
from .models import Job
from company.models import Company

# View for creating a job post
@login_required
def create_job(request):
    # Check if the current user has a company profile
    company = Company.objects.filter(user=request.user).first()
    if not company:
        return redirect('register_company')

    if request.method == 'POST':
        # Extract data from the submitted form
        title = request.POST.get('title')
        description = request.POST.get('description')
        location = request.POST.get('location')
        salary_range = request.POST.get('salary_range')
        tags = request.POST.get('tags')

        # Save the new job post
        Job.objects.create(
            company=company,
            title=title,
            description=description,
            location=location,
            salary_range=salary_range,
            tags=tags
        )

        # Redirect to the job list page
        return redirect('list_jobs')

    # Render the job creation form
    return render(request, 'job/create.html')

# View for listing job posts
@login_required
def list_jobs(request):
    # Check if the current user has a company profile
    company = Company.objects.filter(user=request.user).first()
    if not company:
        return redirect('register_company')

    # Fetch all jobs for the current user's company
    jobs = Job.objects.filter(company=company)

    # Paginate the jobs (2 per page)
    paginator = Paginator(jobs, 2)
    page_number = request.GET.get('page')
    job_page = paginator.get_page(page_number)
    total_pages = job_page.paginator.num_pages

    # Render the job list with pagination
    return render(request, 'job/list.html', {
        'jobs': job_page,
        'total_pages': list(range(1, total_pages + 1))
    })

# View for editing a job post
@login_required
def edit_job(request, job_id):
    # Fetch the job post to be edited, ensure it belongs to the user's company
    job = get_object_or_404(Job, id=job_id, company__user=request.user)

    if request.method == 'POST':
        # Update the job post with new data
        job.title = request.POST.get('title')
        job.description = request.POST.get('description')
        job.location = request.POST.get('location')
        job.salary_range = request.POST.get('salary_range')
        job.tags = request.POST.get('tags')
        job.save()

        # Redirect to the job list page
        return redirect('list_jobs')

    # Render the job editing form
    return render(request, 'job/edit.html', {'job': job})

# View for deleting a job post
@login_required
def delete_job(request, job_id):
    # Fetch the job post to be deleted, ensure it belongs to the user's company
    job = get_object_or_404(Job, id=job_id, company__user=request.user)

    if request.method == 'POST':
        # Delete the job post
        job.delete()

        # Redirect to the job list page
        return redirect('list_jobs')

    # Render the job deletion confirmation page
    return render(request, 'job/delete.html', {'job': job})
