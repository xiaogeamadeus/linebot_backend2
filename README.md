# linebot_backend2
The backend of project "Line_bot"
Created by students in Kyoto University

# setup

1. postgresの導入

2. 仮想環境の作成

```
python -m venv [仮想環境の名前]
```

3. ライブラリのインストール

```
pip install -r requirements.txt
```

4. データベースの作成

データベースのコンソールにはいって以下のSQLを実行

```
CREATE DATABASE linebot_db;
```

5. DBの設定の追加


`local_settings.example.py`をコピーして、`local_settings.py`に変更。DB_XXXの値を設定。


6. マイグレーションの実行

```
python manage.py migrate
```