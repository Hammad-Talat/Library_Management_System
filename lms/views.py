from django.http import HttpResponse,JsonResponse

def home(request):
    print("Request done")
    
    return HttpResponse("This is HomePage")