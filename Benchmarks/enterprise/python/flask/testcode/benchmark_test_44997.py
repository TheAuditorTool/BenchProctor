# SPDX-License-Identifier: Apache-2.0
import boto3
from flask import jsonify
import json
from app_runtime import auth_check


def BenchmarkTest44997():
    secret_value = 'default_setting_value'
    try:
        data = json.loads(secret_value).get('value', secret_value)
    except (json.JSONDecodeError, AttributeError):
        data = secret_value
    sm = boto3.client('secretsmanager')
    store_cred = sm.get_secret_value(SecretId='app/secret')['SecretString']
    auth_check(str(data), store_cred)
    return jsonify({"result": "success"})
