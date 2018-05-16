import base64
import json

import boto3

default_body = {}


class ZappaClient:
    def __init__(self):
        self.client = boto3.client('lambda')

    def invoke(self, function_name, path, data=default_body, http_method="GET", json_response=False):
        payload = self.get_payload(path=path, body=data, http_method=http_method)
        return self.invoke_payload(function_name=function_name, payload=payload, json_response=json_response)

    def invoke_payload(self, function_name, payload, json_response=False):
        return self.parse_response(self.client.invoke(
            FunctionName=function_name,
            InvocationType='RequestResponse',
            LogType='Tail',
            Payload=payload,
        ), json_response=json_response)

    def get_payload(self, path, body=default_body, http_method="POST", headers=None):
        if not headers:
            headers = self.get_headers()
        if type(body) == dict:
            body = json.dumps(body)
        payload = {
            "body": body,
            "headers": headers,
            "pathParameters": {},
            "queryStringParameters": {},
            "requestContext": {},
            "httpMethod": http_method,
            "path": path
        }
        return json.dumps(payload)

    @staticmethod
    def get_headers():
        headers = {
            "Accept-Language": "en-US,en;q=0.8",
            "Accept": "application/json",
            "Accept-Encoding": "gzip, deflate",
            "Content-Type": "application/json"
        }
        return headers

    @staticmethod
    def parse_response(response, json_response=False):
        payload = response['Payload'].read()
        json_body = json.loads(payload.decode())
        body = json_body.get('body', None)

        ret = None
        if body:
            ret = base64.b64decode(body)
            if json_response:
                try:
                    ret = eval(ret)
                except Exception as e:
                    raise ValueError(e)
            else:
                ret = str(ret)

        return ret

    def get_function_environment_variables(self, function_name):
        response = self.client.get_function_configuration(
            FunctionName=function_name
        )
        environment_varibles = response['Environment']['Variables']
        environment_varibles = {str(key): str(environment_varibles[key]) for key in environment_varibles}
        return environment_varibles

    def update_environment_variable(self, function_name, key, value=None):

        environment_variables = self.get_function_environment_varibles(function_name=function_name)
        if value:
            environment_variables[key] = value
        else:
            if key in environment_variables:
                environment_variables.pop(key)
        environment = {'Variables': environment_variables}
        response = self.client.update_function_configuration(FunctionName=function_name, Environment=environment)
        try:
            environment_varibles = response['Environment']['Variables']
            response = {str(key): str(environment_varibles[key]) for key in environment_varibles}
        except Exception as e:
            response = 'Failed to get response: %s' % e
        return response
