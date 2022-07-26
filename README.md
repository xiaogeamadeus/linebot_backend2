# linebot_backend2
The backend of project "Line_bot"
Created by students in Kyoto University

- [Web App](https://lbm.vercel.app/)
- [Front-end repository](https://github.com/yuta-ike/line-bot-maker-front)
- [Presentation](https://docs.google.com/presentation/d/1ppaFRecLssDuJEaxndWJUHQG2cfsEdfi/edit#slide=id.p1)


# tech stack

- Python / Django / PostgreSQL

# setup

1. postgresの導入 / Import the Postgres

2. 仮想環境の作成 / Create the virtual environment

```
python -m venv [the name of virtual environment]
```

3. ライブラリのインストール / Install the requirements environment 

```
pip install -r requirements.txt
```

4. データベースの作成 / Create the database

データベースのコンソールにはいって以下のSQLを実行
Go into the console of database, and run the SQL code below.

```
CREATE DATABASE linebot_db;
```

5. DBの設定の追加 / Add the settings of database


`.env.example`をコピーして、`.env`にrename、正しい値を設定する。

copy the `.env.example` and rename it to`.env`. Then set the right value.


6. マイグレーションの実行 / Migration Execution

```
DJANGO_READ_ENV_FILE=True python manage.py migrate
```

7. 開発サーバの起動
8. 
```
DJANGO_READ_ENV_FILE=True python manage.py runserver 8000
```
