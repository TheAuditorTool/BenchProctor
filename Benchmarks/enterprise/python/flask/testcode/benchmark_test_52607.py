# SPDX-License-Identifier: Apache-2.0
import boto3
import base64
from flask import request, jsonify
from app_runtime import auth_check


def BenchmarkTest52607():
    auth_header = request.headers.get('Authorization', '')
    data = base64.b64decode(auth_header).decode('utf-8', 'ignore')
    sm = boto3.client('secretsmanager')
    store_cred = sm.get_secret_value(SecretId='app/secret')['SecretString']
    auth_check(str(data), store_cred)
    return jsonify({"result": "success"})
