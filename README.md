# Zappa client
This is a tool to call [Zappa](https://github.com/Miserlou/Zappa) functions without APIGateway. 

## Installation 
```
pip install zappa-client
```
 
# Basic Usage
```
from zappa_client import ZappaClient
client = ZappaClient()
client.invoke(function_name=<your-lambda-function-name>,path=<app-route-path>)
```

## Send data
```
from zappa_client import ZappaClient
client = ZappaClient()
client.invoke(function_name=<your-lambda-function-name>, path=<app-route-path>, data={"some":"data"}, http_method="POST")
```

## Except json\dict response
```
from zappa_client import ZappaClient
client = ZappaClient()
client.invoke(function_name=<your-lambda-function-name>, path=<app-route-path>, json_response=True)
```

## Zappa connection 
### Function name 
In the zappa_settings.json file you have the *project_name* and the keys of the file are the "stages", which defines your functions to be `<project_name>-<stage>`
Assuming you deployed the stage "dev" on  *project_name* "test", your function name will be automatically `test-dev`.
You should use `test-dev` as your *function_name* param in the ZappaClient *invoke* function.

### Path
The *path* is the route of your Zappa app handler.
For example, if you use flask, you will use the wrapper `@app.route('/test', methods=['GET'])` to point to a function on zappa.
This is the path we are using. In this case the *path* will be `test` or `/test`. 
 
 

