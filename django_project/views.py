from django.http import HttpResponse
from django.shortcuts import render

def homePage(request):
    # data={
    #     'title':'Home New',
    #     'bdata':'Welcome to india',
    #     'clist':['PHP','Java','Django']
    # }
    return render(request,"Restaurant Website.html")

def aboutUs(request):
    return HttpResponse("welcome to India")

def course(request):
    return HttpResponse("<b>welcome to Raj</b>")

def calculator(request):
    c=''
    try:
        if request.method=="POST":
            n1=eval(request.POST.get('num1'))
            n2=eval(request.POST.get('num2'))
            opr=request.POST.get('opr')
            if opr == '+':
                c=n1+n2
            elif opr == '-':
                c=n1-n2
            elif opr == '*':
                c=n1*n2
            elif opr == '/':
                c=n1/n2            
    except:
        c="invalid opr...."
    print(c)     
    return render(request,"calculator.html",{'c':c})

def courseDetails(request,courseid):
    return HttpResponse(courseid)

def saveevenodd(request):
    c=''
    if request.method=="POST":
        n=eval(request.POST.get('num1'))
        if n%2==0:
            c="Even Number"
        else:
            c="Odd Number"    
    return render(request,"evenodd.html",{'c':c})