import requests
import json
import datetime

def callApi(image_path):
    url = "http://127.0.0.1:8080/example.com/"
    
    sess = requests.session()
    
    print(sess.get(url))
    
    csrftoken = sess.cookies['csrftoken']
    
    # ヘッダ
    headers = {'Content-type': 'application/json',  "X-CSRFToken": csrftoken}
    
    # 送信データ
    prm = {"image_path": image_path}
    
    # JSON変換
    params = json.dumps(prm)
    
    # リクエストのタイムスタンプを取得
    requestTimestamp = datetime.datetime.now(datetime.timezone(datetime.timedelta(hours=9))) 

    # POST送信
    res = sess.post(url, data=params, headers=headers)

    # レスポンスのタイムスタンプを取得
    responseTimestamp = datetime.datetime.now(datetime.timezone(datetime.timedelta(hours=9))) 
 
    # 戻り値を返却
    return json.loads(res.text) , requestTimestamp.strftime('%H%M%S%f') , responseTimestamp.strftime('%H%M%S%f')