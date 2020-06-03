from django.http import HttpResponse
from django.shortcuts import render

def home(request):
    return render(request, 'home.html')

def count(request):
    fulltext = request.GET['fulltext']
    wordlist = fulltext.split()
    
    worddict = {}
    for word in wordlist:
        if word in worddict:
            worddict[word] += 1
        else:
            worddict[word] = 1
    wordtup = sorted(worddict.items(), key = lambda x: x[1], reverse = True)

    return render(request, 'count.html', {'fulltext': fulltext, 'length': len(wordlist), 'wordtup': wordtup})

def about(request):
    return render(request, 'about.html')
