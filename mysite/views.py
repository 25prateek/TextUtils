from django.http import HttpResponse
from  django.shortcuts import render


def index(request):
    return render (request,'index.html')
def analyze(request):
    djtext= request.GET.get('text','default')
    removepunc=request.GET.get('removepunc','off')
    fullcaps = request.GET.get('fullcaps', 'off')
    newlineremover = request.GET.get('newlineremover', 'off')
    extraspaceremover = request.GET.get('extraspaceremover', 'off')
    charcount = request.GET.get('charcount', 'off')
    if removepunc == "on":
        punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
        analyzed =""
        for char in djtext:
            if char not in punctuations:
                analyzed = analyzed + char
        params={'perpose':'removed punctuation','analyzed_text':analyzed}
        #return render(request, 'analyze.html', params)
        djtext = analyzed

    if fullcaps == "on":
        analyzed = ""
        for char in djtext:
            analyzed = analyzed + char.upper()
        params = {'perpose': 'make upper case', 'analyzed_text': analyzed}
        djtext = analyzed
       # return render(request, 'analyze.html', params)

    if newlineremover == "on":
        analyzed = ""
        for char in djtext:
            if char != "\n" and char!="\r":
                analyzed = analyzed + char
            else:
                print("no")
        params = {'perpose': 'remover new line', 'analyzed_text': analyzed}
    #    return render(request, 'analyze.html', params)
        djtext = analyzed

    if extraspaceremover == "on":
        analyzed = ""
        for index,char in enumerate(djtext):
            if not (djtext[index] == " " and djtext[index+1] == " "):
                analyzed = analyzed + char
        params = {'perpose': 'extraspaceremover', 'analyzed_text': analyzed}
        djtext=analyzed

    if charcount == "on":
        analyzed = ""
        i = 0
        for char in djtext:
            i = i + 1
            analyzed = analyzed + char
        analyzed = [analyzed, 'no of count character is :- ', i]
        params = {'perpose': 'no of count is :-', 'analyzed_text': analyzed}
        # return render(request, 'analyze.html', params)
        djtext = analyzed

    if (removepunc != "on" and newlineremover != "on" and extraspaceremover != "on" and fullcaps != "on" and charcount!= "on"):
        return HttpResponse("please select any operation and try again")

    return render(request, 'analyze.html', params)

def about(request):
    return HttpResponse(''' <h1>hiiii</h1><a href="https://www.google.com">Visit google</a> ''')