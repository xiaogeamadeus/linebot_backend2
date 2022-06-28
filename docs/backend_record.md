## Backend's Work


#### Create API
1. Get the user id.
GET /login idToken

2. The list of line_bots which is created by the user.
GET /bot 

3. The details of bot.
GET /bot/:bot_id 

4. Create a new bot.
POST /bot 

5. Renew the detail of bot.
PUT /bot/:bot_id 

6. Delete the bot.
DELETE /bot/:bot_id

7. Activate a user.
POST /user/:user_id

8. Get the message from the user(by line platform)
POST 



#### Create Database 
USER_TABLE
attributes: User_id(LINE USER_ID), name, picture, createdAt

BOT_TABLE
attributes: Bot_id, developerId flowChart, name, createdAt, updateAt

ACTIVATION_TABLE
attributes: Bot_id, User_id(uniqle)

#### Data Structure

block_id
[
 { id:1
   type: "include"
   Output:[
           {label:"yes", node_id:2},
           {label:"no", node_id:3}
          ]
 }


]
