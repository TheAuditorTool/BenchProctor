# SPDX-License-Identifier: Apache-2.0
import boto3
from dataclasses import dataclass
from flask import jsonify
from app_runtime import auth_check


@dataclass
class FormData:
    payload: str

def BenchmarkTest55683():
    with open('/etc/app/app.properties', 'r') as fh:
        prop_value = fh.read()
    data = FormData(payload=prop_value).payload
    sm = boto3.client('secretsmanager')
    store_cred = sm.get_secret_value(SecretId='app/secret')['SecretString']
    auth_check(str(data), store_cred)
    return jsonify({"result": "success"})
