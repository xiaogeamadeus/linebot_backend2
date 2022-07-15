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


`.env.example`をコピーして、`.env`にrename、正しい値を設定する。


6. マイグレーションの実行

```
python manage.py migrate
```