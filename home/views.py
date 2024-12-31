from django.shortcuts import render, redirect
from django.contrib.auth import logout

# Create your views here.
def home(request):

    """

    View to display the home page.

    :param request: The Http request object.

    :return: render the template to display the home page.
    """

 
    if request.method == 'POST':
        logout(request)
        return redirect('signin')

    return render(request, 'home.html')