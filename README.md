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
        "round": 0,
        "started_balance": 100000,
        "bet_size": 5,
        "distribution": "134719123", 
  
        "player": {
                "name": "player",
                "current_balance": 1000,
                "cards": 0.75,
           "status": {
               "code": 0,
               "description": "ready"
           }                 
                
        }
        "opponent": {
           "name": "bot8888",
           "current_balance": 1000,
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

### POST /play/{game_id}/{round}/move/
**params**  
action =  {bet, fold}   
connection_token = your token received using endpoint **/register**      


**response**  
```
{
    "status": 200,
    "data": {
        "game_id": 123123,
        "round": 0,

        
        "player": {
                "name": "player",
                "current_balance": 1000,
                "cards": 0.75,
                "action": "bet",
                "is_winner": true,
           "status": {
               "code": 0,
               "description": "ready"
           }                 
                
        }
        "opponent": {
           "name": "bot8888",
           "current_balance": 1000,
           "cards": -1.0,
           "action": "bet",
           "is_winner": false,
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


