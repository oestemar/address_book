＜プロジェクト概要＞

１．使用技術
　・Python3
　・Flask
　・MySQL
　・Github
　・Railway
　
２．機能一覧（画面構成）
　・登録
　・一覧表示
　・検索
　・CSV読み込み
　・削除

３．フォルダ構成
address_book/
├── README.md   ← ここに置く（必須）
├── app.py
├── requirements.txt
└── templates/
    ├── register.html
    ├── display.html
    ├── search.html
    ├── upload.html
    └── delete.html

４．工夫した点
・Copilot 活用について
・Railway 公開 URL

５．セットアップ手順（Railway / ローカル）
Railway上で動かす場合と、ローカルで動作確認する場合に分けて説明します。

■Railway で動かすためのセットアップ手順
1. プロジェクトをダウンロード
GitHub から ZIP をダウンロードするか、git clone で取得します。

2. GitHub リポジトリにアップロード（任意）
Railway と連携するために、自分の GitHub アカウントへアップロードします。
※GitHub を使わずに Railway の「Upload」機能で ZIP を直接アップロードしても動作します。

3. Railway にログイン
GitHub アカウントで Railway にログインします。

4. Railway でプロジェクトをデプロイ
Railway の「New Project」→「Deploy from GitHub」から、アップロードしたリポジトリを選択します。

5. Flask アプリが起動し、MySQL が自動作成
Railway の自動検出により Flask アプリが起動し、同時に空の MySQL インスタンスが作成されます。
環境変数（DB_HOST / DB_USER / DB_PASSWORD / DB_NAME）は Railway が自動で設定します。

6. CSV を使って初期データを登録
アプリの「CSV アップロード」画面から、会員データを一括登録できます。

CSV の仕様（3 列）
・氏名（漢字）
・電話番号
・住所

7. 各機能を利用	
・登録
・検索
・一覧表示
・CSV アップロード
・削除

■ローカルで動かすためのセットアップ手順
１．プロジェクトをダウンロード（下記①か②）
　①GitHub から ZIP をダウンロード
　②git clone で取得します。
	※git clone https://github.com/oestemar/address_book
	　cd Webapp

２．必要なライブラリをインストールする
　pip install -r requirements.txt

３．ローカル用MySQL準備
　CREATE DATABASE addressbook;

４．app.py の DB 接続設定をローカル用に変更
	db = mysql.connector.connect(
    	host="localhost",
    	user="root",
    	password="あなたのパスワード",
    	database="addressbook"
)

５．Flask を起動
	python app.py

６．ブラウザでアクセス
	http://localhost:5000
	
7. 各機能を利用	
	・登録
	・検索
	・一覧表示
	・CSV アップロード
	・削除


以上