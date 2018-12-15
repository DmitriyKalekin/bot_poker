# bot_poker



### POST /register
**params**
name = Unique name of your bot
pwd = Your password

**response**
```
{
        "status": 200,
        "data": {
            "connection_token": "8ad76f876fd68fa68a6"
        },
        "error": {
        }
}
```
Store connection_token to connect games.


If name already exists:
```
{
    "status": 401,
    "data": { ...  },
    "error": {
        "description": "Name already exists"
    }
```

### POST /play
**params**
connection_token = your token received using endpoint **/register**


**response**
```
{
    "status": 200,
    "data": {
        "game_id": 123123,
        "opponent": {
           "name": "bot8888",
           "status": {
               "code": 0,
               "description": "ready"
           } 
        }
    },
    "error": {
        ...
    }
}
```

