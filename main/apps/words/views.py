from django.shortcuts import render, HttpResponse, redirect
from time import gmtime, strftime

def index(request):
  print "hello"
  if 'current_activity' not in request.session:
        request.session['current_activity'] = []
        print request.session['current_activity']
  return render(request, 'temp/index.html')


def newWord(request):
      print request.POST['word']
      request.session['word'] = request.POST['word']
      request.session['color'] = request.POST['color']
      request.session['font'] = request.POST['font']
      time = strftime("%Y-%m-%d %H:%M %p", gmtime())
      context = {
          'word': request.POST['word'],
          'color': request.POST['color'],
          'font': request.POST['font'],
          'time': time,
      }
      print context
      sessionlist = request.session['current_activity']
      sessionlist.append(context)
      request.session['current_activity'] = sessionlist
      print request.session['current_activity']
      return redirect("/")


