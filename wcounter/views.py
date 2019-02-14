from django.shortcuts import render

# Create your views here.
def index(request):
    
    indexdict = {
        
    }
    return render(request, 'wcounter/index.html',context=indexdict)

def count(request):
    text = request.GET['words']
    words = text.lower().split()
    wordcount = {}
    for word in words:
        if word in wordcount:
            wordcount[word] += 1
        else:
            wordcount.setdefault(word,1)
        
    countdict = {
        'len': len(words),
        'wordcount': wordcount.items(),
        'text':text
    }
    return render(request, 'wcounter/count.html', context=countdict)
    
def about(request):
    
    indexdict = {
        
    }
    return render(request, 'wcounter/about.html',context=indexdict)