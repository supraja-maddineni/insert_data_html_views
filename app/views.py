from django.shortcuts import render
from django.db.models.functions import Length
from django.db.models import Q
# Create your views here.
from app.models import *
def display_topic(request):
    LOT=Topic.objects.all()
    d={'topics':LOT}
    return render(request,'display_topic.html',context=d)

def display_webpage(request):
    LOW=Webpage.objects.all()
    LOW=Webpage.objects.filter(topic_name='cricket')
    #LOW=Webpage.objects.get(topic_name='cricket')
   # LOW=Webpage.objects.get(topic_name='chess')
    #LOW=Webpage.objects.all()[1:2:]
    LOW=Webpage.objects.all().order_by('name')
    LOW=Webpage.objects.all().order_by('-name')
    LOW=Webpage.objects.all().order_by(Length('name'))
    LOW=Webpage.objects.all().order_by(Length('name').desc())
    LOW=Webpage.objects.all()
    LOW=Webpage.objects.filter(name__startswith='d')
    LOW=Webpage.objects.all()
    LOW=Webpage.objects.filter(name__startswith='V')
    LOW=Webpage.objects.all()
    LOW=Webpage.objects.filter(name__endswith='i')
    LOW=Webpage.objects.all()
    LOW=Webpage.objects.filter(name__endswith='sh')
    LOW=Webpage.objects.filter(name__contains='i')
    LOW=Webpage.objects.filter(url__endswith='in')
    LOW=Webpage.objects.filter(topic_name__in=('football','cricket'))
    LOW=Webpage.objects.all()
    #LOW=Webpage.objects.filter(url__in=('virat','rohit'))
    LOW=Webpage.objects.all()
    LOW=Webpage.objects.filter(name__regex='[a-zA-Z]{7}')
    LOW=Webpage.objects.filter(Q(topic_name='cricket')&Q(name='virat'))
    LOW=Webpage.objects.filter(Q(topic_name='Foot Ball'))

    d={'webpage':LOW}
    return render(request,'display_webpage.html',context=d)


def display_accessrecord(request):
    LOA=AccessRecord.objects.all()
    LOA=AccessRecord.objects.filter(date__gt='1991-5-5')
    LOA=AccessRecord.objects.filter(date__lt='1991-5-5')
    LOA=AccessRecord.objects.filter(date__gte='1981-5-5')
    LOA=AccessRecord.objects.filter(date__lte='1991-5-5')
    LOA=AccessRecord.objects.all()
    LOA=AccessRecord.objects.filter(date__year='1988')
    LOA=AccessRecord.objects.all()
    LOA=AccessRecord.objects.filter(date__month='11')
    LOA=AccessRecord.objects.all()
    LOA=AccessRecord.objects.filter(date__day='5')
    LOA=AccessRecord.objects.all()
    LOA=AccessRecord.objects.filter(date__day__gt='5')
    LOA=AccessRecord.objects.filter(date__day__lt='5')
    LOA=AccessRecord.objects.filter(date__month__gt='5')
    LOA=AccessRecord.objects.filter(date__year__gt='1988')

    
    d={'accessrecord':LOA}
    return render(request,'display_accessrecord.html',context=d)