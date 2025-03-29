from django.http import HttpResponse
from django.template import loader
from .models import Member

def members(request):
    mymembers=Member.objects.all().order_by('-id')
    template=loader.get_template('all_members.html')
    context={
        'mymembers':mymembers,
    }
    return HttpResponse(template.render(context,request))

def details(request,slug):
    mymember=Member.objects.get(slug=slug)
    template=loader.get_template('details.html')
    context={
        'mymember':mymember,
    }
    return HttpResponse(template.render(context,request))

def main(request):
    template=loader.get_template("main.html")
    return HttpResponse(template.render())

def testing(request):
    mydata=Member.objects.all()#.filter(firstname='窦')#.values()#.values_list('firstname')#.all()#.values()
    template=loader.get_template('template.html')
    context={
        # 'fruits':['Apple,','Banana','Cherry']
        # 'firstname':'Linus',
        'mymembers':mydata,
    }
    print(mydata)
    return HttpResponse(template.render(context,request))