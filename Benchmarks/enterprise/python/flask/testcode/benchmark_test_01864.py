# SPDX-License-Identifier: Apache-2.0
from cryptography.fernet import Fernet
import boto3
import os
from flask import jsonify


def BenchmarkTest01864():
    env_value = os.environ.get('USER_INPUT', '')
    if env_value:
        data = env_value
    else:
        data = ''
    sm = boto3.client('secretsmanager')
    store_cred = sm.get_secret_value(SecretId='app/secret')['SecretString']
    Fernet(store_cred.encode()).encrypt(str(data).encode())
    return jsonify({"result": "success"})
