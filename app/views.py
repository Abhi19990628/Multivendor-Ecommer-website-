from django.shortcuts import render,redirect 


def Hello(request):
    return render( request, 'hello.html')
def base(request):
    return render(request, 'base.html')




# def BASE(request):
#     return HttpResponse('hello.html')
