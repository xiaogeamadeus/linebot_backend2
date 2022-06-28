## Backend's Work
Member: Ikeoku, Hisatomi, Wang

#### Create API
1. Get the user id.
POST /login idToken/picture
http://localhost/login/getIdToken 
request:"yes"

3. The list of line_bots which is created by the user.
GET /bot 

4. The details of bot.
GET /bot/:bot_id 

5. Create a new bot.
POST /bot 

6. Renew the detail of bot.
PUT /bot/:bot_id 

7. Delete the bot.
DELETE /bot/:bot_id

8. Activate a user.
POST /user/:user_id

9. Get the messages from the user(by line platform)
POST 



#### Create Database 
USER_TABLE
attributes: user_id(LINE USER_ID), name, picture, createdAt

BOT_TABLE
attributes: bot_id, developerId flowChart, name, createdAt, updateAt

ACTIVATION_TABLE
attributes: bot_id, user_id(uniqle)

#### Data Structure


About the flow chart:
type BlockType = string

type FlowChart = [
  {
    id: number,
    type: BlockType,
    values: (string | number)[]
    outputs: number[]
  },
]

const flowChart = [
  {
    id: 0,
    type: "input",
    values: [],
    outputs: [1,],
  },
  {
     id: 1,
     type: "conditional",
     outputs: [2,3],
     values: ["今日"],
  },
  {
    id: 2,
    type: "xxxx",
    outputs: [4],
    values: ["hogehoge"]
  },
  // ...
  {
    id: 4,
    type: "output",
    outputs: [],
    values: [],
  }

]












