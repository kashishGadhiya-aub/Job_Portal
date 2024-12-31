from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Company

# Create your views here.
@login_required
def register_company(request):

    """

    View to register the company of the user.
    """

    if request.method == 'POST':
        name = request.POST.get('name')
        address = request.POST.get('address')
        contact_number = request.POST.get('contact_number')


        if Company.objects.filter(user=request.user).exists():
            return render(request, 'company/register.html', {'error': 'You have already registered a company.'})

     
        company = Company.objects.create(
            user=request.user,
            name=name,
            address=address,
            contact_number=contact_number
        )

       
        return redirect('company_dashboard')

    return render(request, 'company/register.html')


@login_required
def edit_company(request):

    """

    View to edit the company details.
    :return: render the template to edit the details of the company.
    """

  
    company = Company.objects.filter(user=request.user).first()

  
    if not company:
        return redirect('register_company')

   
    if request.method == 'POST':
        company.name = request.POST.get('name')
        company.address = request.POST.get('address')
        company.contact_number = request.POST.get('contact_number')
        company.save()      #
        return redirect('company_dashboard')

    return render(request, 'company/edit.html', {'company': company})

@login_required
def company_dashboard(request):

    """

    View to display the details of the company.

    :return: render the template to display the details of the company.

    """

  
    company = Company.objects.filter(user=request.user).first()

   
    if not company:
        return redirect('register_company')

    return render(request, 'company/dashboard.html', {'company': company})
