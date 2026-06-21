# SPDX-License-Identifier: Apache-2.0
from cryptography.fernet import Fernet
import boto3
from flask import jsonify


class RequestContext:
    def __init__(self, payload):
        self.payload = payload

def BenchmarkTest49862():
    with open('/etc/app/app.properties', 'r') as fh:
        prop_value = fh.read()
    ctx = RequestContext(prop_value)
    data = ctx.payload
    sm = boto3.client('secretsmanager')
    store_cred = sm.get_secret_value(SecretId='app/secret')['SecretString']
    Fernet(store_cred.encode()).encrypt(str(data).encode())
    return jsonify({"result": "success"})
