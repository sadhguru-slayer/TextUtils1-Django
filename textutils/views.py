from django.http import HttpResponse
from django.shortcuts import render

#def index(request):
 #   return HttpResponse("So How's it going on \n Just coded")

def djangoL(request):

   t=request.GET.get('text','default')
   capall=request.GET.get('capall','off')
   puncrem = request.GET.get('puncrem', 'off')
   spacerem = request.GET.get('spacerem', 'off')
   newlinerem = request.GET.get('newlinerem', 'off')
   coun_tit = request.GET.get('coun_tit', 'off')
   # Capitallizinng every F-king letter
   if capall == 'on':
       L = ''
       for char in t:
           L = L + char.upper()
       dict = {'head': 'After CAPITALIZING Letters', 'work': L}
       t=L

   if puncrem=='on':
       p='''`!@#$%^&*()-=][';/.,{}\:"?><'''
       L=""
       for char in t:

           if char not in p:

               L=L+char
       dict = {'head':'After removing Punctuations','work': L}
       t=L
       #return render(request,'djangoL.html',dict)#,HttpResponse('''<hr><br><br><h1>Lotes</h1> <a href="https://www.youtube.com/watch?v=5BDgKJFZMl8&list=PLu0W_9lII9ah7DDtYtflgwMwpT3xmjXY9" target="_main"> Django Harry</a> <small> <a href="/"> <small>Go Back<small> </a></small>''')

   #Removing every F-king new line
   if newlinerem=='on':
       L=''
       for char in t:
           if char !='\n':

               L=L+char
       dict = {'head': 'After Removing New Line', 'work': L}
       t=L
       #return render(request,'djangoL.html',dict)
   #F***k the spaces
   if spacerem=='on':
       L=''
       for char in t:
           if char !=' ' or '  '  or '    ' or '     ' or  '      ':

               L=L+char
       dict = {'head': 'After Removing spaces', 'work': L}
       t=L
       #return render(request,'djangoL.html',dict)


   if coun_tit=='on':

       L=len(t)

       dict = {'head': 'Characters count is', 'work': L}

       #return render(request,'djangoL.html',dict)
   if puncrem!='on' and spacerem!='on' and capall!="on" and coun_tit!="on" and newlinerem != 'on':
         return HttpResponse("Choose your words wisely...Baka")

   return render(request,'djangoL.html',dict)

def mychannel(request):
     return render(request,'index.html')

def c(request):
    return render(request,'bb.html')

def txtutil(request):
    return render(request,'txtutil.html')