# address_book – 住所録管理システム

Flask と MySQL を使用した住所録管理システムです。  
ユーザー情報（氏名・電話番号・住所）の **登録・検索・表示・削除・CSV インポート** が可能です。

---

## 🚀 機能一覧

- ユーザー登録（Create）
- ユーザー一覧表示（Read）
- ユーザー検索（Read）
- ユーザー削除（Delete）
- CSV インポート（複数件一括登録）
- MySQL 自動接続（ローカル / 本番切り替え）

---

## 🗂 画面一覧

- `/` … TOP メニュー
- `/register` … 登録画面
- `/display` … 一覧表示
- `/search` … 検索
- `/delete` … 削除
- `/upload` … CSV インポート

---

## 🧱 使用技術

- Python 3.x
- Flask
- MySQL
- Railway（ホスティング）
- Jinja2（テンプレート）
- CSS（static/style.css）
- python-dotenv（環境変数管理）

---

## 📁 ディレクトリ構成

address_book/
│  app.py
│  .env
│  README.md
│  requirements.txt
│
├─static/
│      style.css
│
├─templates/
│      index.html
│      register.html
│      display.html
│      search.html
│      delete.html
│      upload.html

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
環境変数（DATABASE_URL,PORT, SECRET_KEY）は 自分で設定します。

6. CSV を使って初期データを登録
アプリの「CSV アップロード」画面から、会員データを一括登録できます。

CSV の仕様（3 列）
・氏名（漢字）
・電話番号
・住所

7. 各機能を利用	
・登録
・一覧表示
・検索
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
　CREATE DATABASE address_book;

４．app.py の DB 接続設定（.envファイル）を自分のローカル環境用に変更

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