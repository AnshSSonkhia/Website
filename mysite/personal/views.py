from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, 'personal/home.html') # return render(request, 'personal/home.html')  will
                                                #  look for html file into template directory and hence we have
                                                # to make a new one ourself and make personal/home.html in it
def contact(request):
    return render(request, 'personal/basic.html', {'content':['If you like to contact me, please email me at','harsh_goel@ymail.com']})