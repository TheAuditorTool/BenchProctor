# SPDX-License-Identifier: Apache-2.0
import boto3
from flask import jsonify
from app_runtime import auth_check


request_state: dict[str, str] = {}

def BenchmarkTest26962():
    secret_value = 'default_config_label'
    request_state['last_input'] = secret_value
    data = request_state['last_input']
    sm = boto3.client('secretsmanager')
    store_cred = sm.get_secret_value(SecretId='app/secret')['SecretString']
    auth_check(str(data), store_cred)
    return jsonify({"result": "success"})
