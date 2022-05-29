from django.http import HttpResponse
from django.template import loader
from .models import AiAnalysisLog  
from datetime import datetime as dt

def input(request):
    template = loader.get_template("sample_app/input.html")
    return HttpResponse(template.render({}, request))

def output(request):
    image_path = request.POST["image_path"]
    template = loader.get_template("sample_app/output.html")
    context = {
        "image_class": image_path,
    }

    aiAnalysisLog = AiAnalysisLog()
    aiAnalysisLog.image_path = image_path
    aiAnalysisLog.save()
    return HttpResponse(template.render(context, request))