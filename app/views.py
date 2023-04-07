from django.shortcuts import render
from django.db.models.functions import Length

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
    d={'webpage':LOW}
    return render(request,'display_webpage.html',context=d)


def display_accessrecord(request):
    LOA=AccessRecord.objects.all()
    LOA=AccessRecord.objects.filter(date__gt='1991-5-5')
    LOA=AccessRecord.objects.filter(date__lt='1991-5-5')
    LOA=AccessRecord.objects.filter(date__gte='1981-5-5')
    LOA=AccessRecord.objects.filter(date__lte='1991-5-5')
    d={'accessrecord':LOA}
    return render(request,'display_accessrecord.html',context=d)