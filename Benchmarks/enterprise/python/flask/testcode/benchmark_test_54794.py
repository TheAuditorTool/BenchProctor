# SPDX-License-Identifier: Apache-2.0
import boto3
from flask import jsonify
import os
from app_runtime import auth_check


request_state: dict[str, str] = {}

def BenchmarkTest54794():
    dotenv_value = os.environ.get('DOTENV_VAR', '')
    request_state['last_input'] = dotenv_value
    data = request_state['last_input']
    sm = boto3.client('secretsmanager')
    store_cred = sm.get_secret_value(SecretId='app/secret')['SecretString']
    auth_check(str(data), store_cred)
    return jsonify({"result": "success"})
