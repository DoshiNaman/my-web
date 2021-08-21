from django.shortcuts import render, HttpResponse
from datetime import date, datetime
from home.models import Contact
from django.contrib import messages
from blog.models import Post
from home.models import Work,Info,Education,Job,Services,Social,Achievement

# Create your views here.
def index(request):
    #messages.success(request,"Test msg")
    if request.method == "POST":
        name=request.POST.get('name')
        email=request.POST.get('email')
        project=request.POST.get('project')
        msg=request.POST.get('msg')
        contact=Contact(name=name,email=email,project=project,msg=msg,date=datetime.today())
        contact.save()
        messages.success(request,'Your message has been sent !')
    
    allPosts= Post.objects.all().order_by('-timeStamp')[:3]
    allWorks= Work.objects.all().order_by('-date')[:3]
    info= Info.objects.all().first()
    education=Education.objects.all()
    job=Job.objects.all().order_by('-title')
    services=Services.objects.all()
    social=Social.objects.all()
    achievements=Achievement.objects.all().order_by('-achiev_year')
   
    context={'allPosts': allPosts,'allWorks': allWorks,'info':info,'education':education,'job':job,'services':services,'social':social,'achievements':achievements}
    return render(request,"index.html", context)
    #return HttpResponse("This is home page")


def cv(request):
    return render(request,"cv/index.html")

def find(request):
    if request.method == "POST":
        searched = request.POST.get('searched')
        if len(searched)>78:
            allPosts=Post.objects.none()
        else:
            allPostsTitle= Post.objects.filter(title__icontains=searched)
            allPostsAuthor= Post.objects.filter(author__icontains=searched)
            allPosts=  allPostsTitle.union(allPostsAuthor)
        if allPosts.count()==0:
            messages.warning(request, "No search results found. Please refine your query.")
        params={'allPosts': allPosts, 'searched': searched}
        
        return render(request, 'cv/search.html',params) 
