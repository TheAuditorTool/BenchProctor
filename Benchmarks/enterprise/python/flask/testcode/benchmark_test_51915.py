# SPDX-License-Identifier: Apache-2.0
from cryptography.fernet import Fernet
import boto3
from dataclasses import dataclass
import os
from flask import jsonify


@dataclass
class FormData:
    payload: str

def BenchmarkTest51915():
    env_value = os.environ.get('USER_INPUT', '')
    data = FormData(payload=env_value).payload
    sm = boto3.client('secretsmanager')
    store_cred = sm.get_secret_value(SecretId='app/secret')['SecretString']
    Fernet(store_cred.encode()).encrypt(str(data).encode())
    return jsonify({"result": "success"})
