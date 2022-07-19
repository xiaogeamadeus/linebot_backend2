## Backend's Work
Member: Ikeoku, Hisatomi, Wang

#### Create API for frontend
1. Get the user id.(optional)
POST /login idToken
http://localhost/login/getIdToken 
request:"yes"

2. The list of line_bots which is created by the user. (success)
GET getIdToken/bot 

3. The details of bot. (success)
GET getIdToken/bot/:bot_id 

4. Create a new bot. (success)
POST getIdToken/bot 
{
"bot_id":"",
"name":"",
"developerId":"",
"flowChart":"",
}

5. Renew the detail of bot. (success)
PUT getIdToken/bot/:bot_id
{
}

6. Delete the bot. (success)
DELETE getIdToken/bot/:bot_id

7. Activate a user. (success)
POST getIdToken/activate
{
"user_id":"", 
"bot_id":""
}



#### Connecting with Line Platform(message API)
When user send some message or follow your official account, The line platform will send a POST request to your server.
1. Get messages/follow information from the user(by line platform)
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












