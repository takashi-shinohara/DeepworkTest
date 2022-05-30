

from .models import AiAnalysisLog  

def insertAiAnalysisLog(imagePath , insertData , requestTimestamp , responseTimestamp):
   # DB登録
    aiAnalysisLog = AiAnalysisLog()
    aiAnalysisLog.image_path = imagePath
    aiAnalysisLog.success = insertData.get("success")
    aiAnalysisLog.message = insertData.get("message")
    aiAnalysisLog.class_field = insertData.get("estimated_data").get("class")
    aiAnalysisLog.confidence = insertData.get("estimated_data").get("confidence")
    aiAnalysisLog.request_timestamp = requestTimestamp[0:10]
    aiAnalysisLog.response_timestamp = responseTimestamp[0:10]
    aiAnalysisLog.save()
