# SPDX-License-Identifier: Apache-2.0
import jwt
import boto3
from flask import jsonify


def BenchmarkTest11676():
    secret_value = 'feature_flag_value'
    data = f'{secret_value}'
    sm = boto3.client('secretsmanager')
    store_cred = sm.get_secret_value(SecretId='app/secret')['SecretString']
    jwt.encode({'sub': str(data)}, store_cred, algorithm='HS256')
    return jsonify({"result": "success"})
