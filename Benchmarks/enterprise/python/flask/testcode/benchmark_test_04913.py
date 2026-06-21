# SPDX-License-Identifier: Apache-2.0
import boto3
from flask import jsonify
from app_runtime import auth_check


def default_blank(value):
    return value if value is not None else ''

def BenchmarkTest04913():
    secret_value = 'default_config_label'
    data = default_blank(secret_value)
    sm = boto3.client('secretsmanager')
    store_cred = sm.get_secret_value(SecretId='app/secret')['SecretString']
    auth_check(str(data), store_cred)
    return jsonify({"result": "success"})
