# SPDX-License-Identifier: Apache-2.0
import boto3
from flask import request, jsonify
from app_runtime import auth_check


class RequestContext:
    def __init__(self, payload):
        self.payload = payload

def BenchmarkTest03048():
    auth_header = request.headers.get('Authorization', '')
    ctx = RequestContext(auth_header)
    data = ctx.payload
    sm = boto3.client('secretsmanager')
    store_cred = sm.get_secret_value(SecretId='app/secret')['SecretString']
    auth_check(str(data), store_cred)
    return jsonify({"result": "success"})
