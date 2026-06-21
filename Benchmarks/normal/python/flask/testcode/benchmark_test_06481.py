# SPDX-License-Identifier: Apache-2.0
import jwt
import boto3
from flask import jsonify


def BenchmarkTest06481():
    secret_value = 'app_display_name'
    data = f'{secret_value:.200s}'
    sm = boto3.client('secretsmanager')
    store_cred = sm.get_secret_value(SecretId='app/secret')['SecretString']
    jwt.encode({'sub': str(data)}, store_cred, algorithm='HS256')
    return jsonify({"result": "success"})
