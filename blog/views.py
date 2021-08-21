from django.shortcuts import render, HttpResponse, redirect
from blog.models import Post, BlogComment
from django.contrib import messages
from blog.templatetags import extras 
from django.contrib.auth.models import User 
from django.contrib.auth  import authenticate,  login, logout

# Create your views here.
def blogHome(request): 
    allPosts= Post.objects.all().order_by('-timeStamp')
    context={'allPosts': allPosts}
    return render(request, "blog/blogHome.html", context)

def blogPost(request, slug): 
    post=Post.objects.filter(slug=slug).first()
    post.views= post.views +1
    post.save()
    #products = Post.objects.filter(slug=slug).first()

    comments= BlogComment.objects.filter(post=post, parent=None)
    replies= BlogComment.objects.filter(post=post).exclude(parent=None)
    replyDict={}
    for reply in replies:
        if reply.parent.sno not in replyDict.keys():
            replyDict[reply.parent.sno]=[reply]
        else:
            replyDict[reply.parent.sno].append(reply)

    context={'post':post, 'comments': comments, 'user': request.user, 'replyDict': replyDict, }
    return render(request, "blog/blogPost.html", context)

def postComment(request):
    if request.method == "POST":
        comment=request.POST.get('comment')
        user=request.user
        postSno =request.POST.get('postSno')
        post= Post.objects.get(sno=postSno)
        parentSno= request.POST.get('parentSno')
        if parentSno=="":
            comment=BlogComment(comment= comment, user=user, post=post)
            comment.save()
            messages.success(request, "Your comment has been posted successfully")
        else:
            parent= BlogComment.objects.get(sno=parentSno)
            comment=BlogComment(comment= comment, user=user, post=post , parent=parent)
            comment.save()
            messages.success(request, "Your reply has been posted successfully")
        
    return redirect(f"/blog/{post.slug}")



def handleSignUp(request):
    if request.method=="POST":
        # Get the post parameters
        username=request.POST['username']
        email=request.POST['email']
        fname=request.POST['fname']
        lname=request.POST['lname']
        pass1=request.POST['pass1']
        pass2=request.POST['pass2']

        # check for errorneous input
        if len(username)>10:
            messages.error(request, " Your user name must be under 10 characters")
            return redirect('/blog')

        if not username.isalnum():
            messages.error(request, " User name should only contain letters and numbers")
            return redirect('/blog')

        if (pass1!= pass2):
             messages.error(request, " Passwords do not match")
             return redirect('/blog')
        
        # Create the user
        myuser = User.objects.create_user(username, email, pass1)
        myuser.first_name= fname
        myuser.last_name= lname
        myuser.save()
        messages.success(request, " Your iCoder has been successfully created")
        return redirect('/blog')

    else:
        return HttpResponse("404 - Not found")

def handeLogin(request):
    if request.method=="POST":
        # Get the post parameters
        loginusername=request.POST['loginusername']
        loginpassword=request.POST['loginpassword']

        user=authenticate(username= loginusername, password= loginpassword)
        if user is not None:
            login(request, user)
            messages.success(request, "Successfully Logged In")
            return redirect("/blog")
        else:
            messages.error(request, "Invalid credentials! Please try again")
            return redirect("/blog")

    return HttpResponse("404- Not found")
   

    return HttpResponse("login")

'''
{% for soc in social  %}
              {% if soc.title == 'dribble' %}
              
              {% elif soc.title == 'linkedin' %}
              
              {% else %}
              <a href="{{soc.link}}" target="_blank" class="footer__social">
                <i class="uil {{soc.icon}}"></i>
              </a>
              {% endif %}
            {% endfor %}
'''
def handelLogout(request):
    logout(request)
    messages.success(request, "Successfully logged out")
    return redirect('/blog')
