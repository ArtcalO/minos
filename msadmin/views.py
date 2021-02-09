from django.shortcuts import render

# Create your views here.
def homeAdmin(request):
	dashboard = True
	return render(request, 'admin-home.html', locals())

def validatedAdmin():
	validatedAdmin = True

	return render(request, 'admin-validated.html', locals())