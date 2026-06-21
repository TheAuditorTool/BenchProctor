# SPDX-License-Identifier: Apache-2.0
from cryptography.fernet import Fernet
import boto3
from dataclasses import dataclass
from flask import request, jsonify


@dataclass
class FormData:
    payload: str

def BenchmarkTest12217():
    header_value = request.headers.get('X-Custom-Header', '')
    data = FormData(payload=header_value).payload
    sm = boto3.client('secretsmanager')
    store_cred = sm.get_secret_value(SecretId='app/secret')['SecretString']
    Fernet(store_cred.encode()).encrypt(str(data).encode())
    return jsonify({"result": "success"})
