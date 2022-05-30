### django + pythonで処理を作成しました。

ローカルサーバ起動コマンド<br>
  python manage.py runserver 0.0.0.0:8080

### 以下のローカルURLから画像パスを入力し送信する事で処理が起動します。<br>
  http://localhost:8080/sample/

  ※画像パスを未入力のまま送信を行うとエラー画面に遷移します。<br>


### 処理は以下に区分けして作成しました。<br>
  API呼び出：requestAI.py <br>
  ダミーAPI：responseAI.py <br>
  データ登録：dao.py

データベースはMySQlを使用して動作確認を行っております。
