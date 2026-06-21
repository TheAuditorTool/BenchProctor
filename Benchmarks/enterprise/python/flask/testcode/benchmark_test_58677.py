# SPDX-License-Identifier: Apache-2.0
import boto3
from flask import jsonify
from app_runtime import auth_check


class RequestContext:
    def __init__(self, payload):
        self.payload = payload

def BenchmarkTest58677():
    secret_value = 'feature_flag_value'
    ctx = RequestContext(secret_value)
    data = ctx.payload
    sm = boto3.client('secretsmanager')
    store_cred = sm.get_secret_value(SecretId='app/secret')['SecretString']
    auth_check(str(data), store_cred)
    return jsonify({"result": "success"})
