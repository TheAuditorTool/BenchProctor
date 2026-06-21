# SPDX-License-Identifier: Apache-2.0
import boto3
from flask import request, jsonify
from app_runtime import auth_check


def BenchmarkTest14350():
    graphql_var = (request.get_json(silent=True) or {}).get('variables', {}).get('input', '')
    sm = boto3.client('secretsmanager')
    store_cred = sm.get_secret_value(SecretId='app/secret')['SecretString']
    auth_check(str(graphql_var), store_cred)
    return jsonify({"result": "success"})
