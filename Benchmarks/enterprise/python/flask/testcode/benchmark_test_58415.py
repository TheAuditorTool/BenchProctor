# SPDX-License-Identifier: Apache-2.0
import boto3
from flask import request, jsonify
from app_runtime import auth_check


def BenchmarkTest58415():
    header_value = request.headers.get('X-Custom-Header', '')
    data = bytes.fromhex(header_value).decode('utf-8', 'ignore')
    sm = boto3.client('secretsmanager')
    store_cred = sm.get_secret_value(SecretId='app/secret')['SecretString']
    auth_check(str(data), store_cred)
    return jsonify({"result": "success"})
