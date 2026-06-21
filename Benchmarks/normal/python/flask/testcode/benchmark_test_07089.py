# SPDX-License-Identifier: Apache-2.0
from cryptography.fernet import Fernet
import boto3
from flask import jsonify


request_state: dict[str, str] = {}

def BenchmarkTest07089():
    secret_value = 'default_setting_value'
    request_state['last_input'] = secret_value
    data = request_state['last_input']
    sm = boto3.client('secretsmanager')
    store_cred = sm.get_secret_value(SecretId='app/secret')['SecretString']
    Fernet(store_cred.encode()).encrypt(str(data).encode())
    return jsonify({"result": "success"})
