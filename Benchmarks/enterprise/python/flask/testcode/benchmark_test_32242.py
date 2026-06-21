# SPDX-License-Identifier: Apache-2.0
import boto3
from dataclasses import dataclass
import os
from flask import jsonify
from app_runtime import auth_check


@dataclass
class FormData:
    payload: str

def BenchmarkTest32242():
    env_value = os.environ.get('USER_INPUT', '')
    data = FormData(payload=env_value).payload
    sm = boto3.client('secretsmanager')
    store_cred = sm.get_secret_value(SecretId='app/secret')['SecretString']
    auth_check(str(data), store_cred)
    return jsonify({"result": "success"})
