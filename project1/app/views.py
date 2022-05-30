from django.http import HttpResponse
from django.template import loader
from .requestAI import callApi  
from .dao import insertAiAnalysisLog  

def input(request):
    template = loader.get_template("sample_app/input.html")
    return HttpResponse(template.render({}, request))

def output(request):
    image_path = request.POST["image_path"]
    template = loader.get_template("sample_app/output.html")

    # API呼び出し
    res , requestTime , responceTime = callApi(image_path)

    # DB登録
    insertAiAnalysisLog(image_path , res , requestTime, responceTime)
    if res.get("success") == "false" :
        template = loader.get_template("sample_app/error.html")

    # クラスを設定
    context = {
        "image_class": res.get("estimated_data").get("class"),
    }

    return HttpResponse(template.render(context, request))

