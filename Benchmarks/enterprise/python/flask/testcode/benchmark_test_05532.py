# SPDX-License-Identifier: Apache-2.0
from cryptography.fernet import Fernet
import boto3
import json
from flask import request, jsonify


def BenchmarkTest05532():
    json_value = (request.get_json(silent=True) or {}).get('payload', '')
    data = json.loads(json_value).get('value', '')
    sm = boto3.client('secretsmanager')
    store_cred = sm.get_secret_value(SecretId='app/secret')['SecretString']
    Fernet(store_cred.encode()).encrypt(str(data).encode())
    return jsonify({"result": "success"})
