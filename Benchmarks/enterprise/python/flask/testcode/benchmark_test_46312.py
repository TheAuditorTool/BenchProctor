# SPDX-License-Identifier: Apache-2.0
import boto3
from flask import jsonify
import ast
from app_runtime import auth_check


def BenchmarkTest46312():
    secret_value = 'default_config_label'
    try:
        data = str(ast.literal_eval(secret_value))
    except (ValueError, SyntaxError):
        data = secret_value
    sm = boto3.client('secretsmanager')
    store_cred = sm.get_secret_value(SecretId='app/secret')['SecretString']
    auth_check(str(data), store_cred)
    return jsonify({"result": "success"})
