# SPDX-License-Identifier: Apache-2.0
import jwt
import boto3
from flask import jsonify


def BenchmarkTest39040():
    secret_value = 'app_display_name'
    data, _sep, _rest = str(secret_value).partition('\x00')
    sm = boto3.client('secretsmanager')
    store_cred = sm.get_secret_value(SecretId='app/secret')['SecretString']
    jwt.encode({'sub': str(data)}, store_cred, algorithm='HS256')
    return jsonify({"result": "success"})
