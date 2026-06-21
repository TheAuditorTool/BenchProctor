# SPDX-License-Identifier: Apache-2.0
import boto3
from dataclasses import dataclass
from flask import jsonify
import os
from app_runtime import auth_check


@dataclass
class FormData:
    payload: str

def BenchmarkTest49052():
    dotenv_value = os.environ.get('DOTENV_VAR', '')
    data = FormData(payload=dotenv_value).payload
    sm = boto3.client('secretsmanager')
    store_cred = sm.get_secret_value(SecretId='app/secret')['SecretString']
    auth_check(str(data), store_cred)
    return jsonify({"result": "success"})
