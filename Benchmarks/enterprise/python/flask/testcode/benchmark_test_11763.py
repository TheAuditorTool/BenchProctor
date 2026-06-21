# SPDX-License-Identifier: Apache-2.0
import boto3
from flask import jsonify
import ast
from app_runtime import auth_check


def BenchmarkTest11763():
    with open('/tmp/data', 'r') as fh:
        file_value = fh.read()
    try:
        data = str(ast.literal_eval(file_value))
    except (ValueError, SyntaxError):
        data = file_value
    sm = boto3.client('secretsmanager')
    store_cred = sm.get_secret_value(SecretId='app/secret')['SecretString']
    auth_check(str(data), store_cred)
    return jsonify({"result": "success"})
