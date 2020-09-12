from django.http import HttpResponse
from django.shortcuts import render


def index(request):
    return render(request, 'index.html')

def analyze(request):
    djtext = request.POST.get('text', 'default')
    removepunc = request.POST.get('removepunc', 'off')
    fullcaps = request.POST.get('fullcaps', 'off')
    if removepunc == "on":
        analyzed = ""
        punctuations = ''':;%-[{}()<>'*+?.\,^$|#]/,"$&"'''
        for char in djtext:
            if char not in  punctuations:
                analyzed = analyzed + char
        params = {'purpose': 'Removed Punctuations', 'analyzed_text': analyzed}
        djtext = analyzed

    if (fullcaps=='on'):
        analyzed = ""
        for char in djtext:
            analyzed = analyzed + char.upper()

        params = {'purpose': 'Changed to uppercase', 'analyzed_text': analyzed}

    if (removepunc != "on" and fullcaps != "on"):
        return HttpResponse("error:you don't select any of it's choice")

    return render(request, 'analyze.html', params)
