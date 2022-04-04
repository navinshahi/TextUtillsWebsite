# i have created this website - Navin Shahi
from django.http import HttpResponse
from django.shortcuts import render

# Code for video 6 :
# def index(request):
#     return HttpResponse('''<h1>Hello Navin</h1><a href="https://hybridcalculator.xyz">Hybrid Calculator</a>''')
# def about(request):
#     return HttpResponse("About Navin")

# Code for video 8 :
def index(request):
    return render(request,"index.html")
def Analyze(request):
    #get the text
    djtext=request.POST.get('text','default')
    removepunc=request.POST.get('removepunc','off')
    fullcaps=request.POST.get('fullcaps','off')
    newlineremover=request.POST.get('newlineremover','off')
    extraspaceremover=request.POST.get('extraspaceremover','off')
    charactercounter=request.POST.get('charactercounter','off')
    originaltext=djtext
    analyzed=""
    cnt=0
    status1=""
    k=0
    if removepunc=="on":
        analyzed=""
        if k==0:
            status1+="Remove Punctuation + "
        elif k==1:
            status1+="Remove Punctuation"
        else:
            status1+="+ Remove Punctuation"
        k+=1
        punctuations='''!()-[]{};:'"\,<>./?@#$%^&*_~'''
        for char in djtext:
            if char not in punctuations:
                analyzed+=char 
        djtext=analyzed
    if fullcaps=="on":
        analyzed=""
        if k==0:
            status1+="Change to Uppercase + "
        elif k==1:
            status1+="Change to Uppercase"
        else:
            status1+="+ Change to Uppercase"
        k+=1
        for char in djtext:
            analyzed+=char.upper()
        djtext=analyzed
    if newlineremover=="on":
        analyzed=""
        if k==0:
            status1+="New Line Remover + "
        elif k==1:
            status1+="New Line Remover"
        else:
            status1+="+ New Line Remover"
        k+=1
        for char in djtext:
            if char!="\n":
                analyzed+=char
        djtext=analyzed
    if extraspaceremover=="on":
        analyzed=""
        if k==0:
            status1+="Extra Space Remover + "
        elif k==1:
            status1+="Extra Space Remover"
        else:
            status1+="+ Extra Space Remover"
        k+=1
        n=len(djtext)
        for i in range(0,n-1):
            if djtext[i]==" " and djtext[i+1]==" ":
                pass
            else:
                analyzed+=djtext[i]
        djtext=analyzed
    if charactercounter=="on":
        if k==0:
            status1+="Character Counter + "
        elif k==1:
            status1+="Character Counter"
        else:
            status1+="+ Character Counter"
        k+=1
        for char in djtext:
            if char!=" ":
                cnt+=1
    if removepunc=="on" or fullcaps=="on" or newlineremover=="on" or extraspaceremover=="on" or charactercounter=="on":
        if charactercounter=="on":
            djtext+=" , Character Count:- "+str(cnt)
        params={"purpose":status1,"Analyzed_Text":djtext,"mytext":originaltext}
        #analyze the text
        return render(request,"analyze.html",params)
    else:
        return HttpResponse("Error")

# def capfirst(request):
#     return HttpResponse("capfirst")
# def newlineremove(request):
#     return HttpResponse("newlineremove")
# def spaceremover(request):
#     return HttpResponse("spaceremover")
# def charcount(request):
#     return HttpResponse("charcount")