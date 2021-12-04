from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    return render(request, 'index.html')

def analyze(request):
    djtext=request.POST.get('text','default')
    removepunc=request.POST.get('removepunc','off')
    capitalize=request.POST.get('capitalize','off')
    charcount=request.POST.get('charcount','off')
    extraspace=request.POST.get('extraspace','off')
    
    if removepunc =="on" or capitalize =="on" :
        analyze=''
        punc= '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
        for char in djtext:
            if char not in punc:
                analyze=analyze+char
        params= {'purpose': 'Removing punctuation', 'analyzed_text':analyze}
        djtext=analyze
        

    if capitalize =="on":
        analyze=''
        for i in djtext:
            analyze=analyze+i.upper()
        params= {'purpose': 'Capitalize text', 'analyzed_text':analyze}
        djtext=analyze
       
    
    if extraspace == "on":
        analyze=''
        for i,item in enumerate(djtext):
            if not (djtext[i] ==" " and djtext[i+1] == " "):
                analyze=analyze+item        
        params= {'purpose': 'Removing extra space', 'analyzed_text':analyze}
        djtext=analyze
    
    if(removepunc != "on" and extraspace!="on" and capitalize!="on"):
        return HttpResponse("please select any operation and try again")

    if charcount == "on":
        count=0
        for char in djtext:
            count=count+1
        params= {'purpose': 'Count length', 'analyzed_text':count}
        djtext=analyze
    return render(request,'analyze.html',params)

    
 


    
    






