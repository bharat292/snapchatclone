from django.shortcuts import render
def image_view(request):
	image = request.POST.get('value')
	return render(request,'front.html')
# Create your views here.
