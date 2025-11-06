from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/',methods=['GET', 'POST']) # POSTリクエストも受け取れるように変更。これにより、フォームの送信を処理できるようになった
def home():
    car_name = None #変数を初期化
    manufacturer_name = None
    user_comment = None

    if request.method == 'POST': # ウェブサイトのアクセスがフォームの送信(POST)だったら、次の処理。
        # フォームから'car'という名前のデータを取得　→　get()メソッドはフォームの<input>タグに設定されたname属性(ここではname="car")をキーとして、その値を取得する
        manufacturer_name = request.form.get('manufacturer')
        car_name = request.form.get('car')
        user_comment = request.form.get('comment')
        # ターミナルに取得したデータを表示
        print("---フォーム送信データ---")
        print(f"自動車メーカー：{manufacturer_name}")
        print(f"ユーザーが入力した自動車：{car_name}")
        print(f"コメント：{user_comment}")
        print("------------------------")
        # fは文字列の中に変数の値を簡単に埋め込むための書き方
        # f文字列を使うと、{}の中に直接変数を書くことができる

    return render_template(
        'index.html', 
        manufacturer_name=manufacturer_name,
        car_name=car_name,
        user_comment=user_comment #新しい変数をHTMLに渡す
    )


# Flaskアプリケーションが実行されたときだけサーバーを起動する
if __name__ == '__main__': 

    app.run(debug=True)   # .run()はFlaskの開発用サーバーを起動するメソッド　#debug=Tureをつけると、コードを変更すると自動でリロードされる(再起動させなくていい),エラー発生時にブラウザにデバッグ画面が出る。

"""
    上記はFlaskというフレームワークを使ってWebサーバを起動して、ユーザーが「/」というURLにアクセスすると、templatesフォルダ内のindex.htmlを返すというシンプルな動作を定義する。
"""