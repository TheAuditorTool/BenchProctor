# SPDX-License-Identifier: Apache-2.0
import boto3
from flask import jsonify
from app_runtime import auth_check


def relay_value(value):
    return value

def BenchmarkTest50008():
    with open('/etc/app/app.properties', 'r') as fh:
        prop_value = fh.read()
    data = relay_value(prop_value)
    sm = boto3.client('secretsmanager')
    store_cred = sm.get_secret_value(SecretId='app/secret')['SecretString']
    auth_check(str(data), store_cred)
    return jsonify({"result": "success"})
