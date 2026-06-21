# SPDX-License-Identifier: Apache-2.0
from cryptography.fernet import Fernet
import boto3
from flask import request, jsonify


def BenchmarkTest54350():
    host_value = request.headers.get('Host', '')
    if host_value:
        data = host_value
    else:
        data = ''
    sm = boto3.client('secretsmanager')
    store_cred = sm.get_secret_value(SecretId='app/secret')['SecretString']
    Fernet(store_cred.encode()).encrypt(str(data).encode())
    return jsonify({"result": "success"})
