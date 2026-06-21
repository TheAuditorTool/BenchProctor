# SPDX-License-Identifier: Apache-2.0
import boto3
from flask import jsonify
import json
from app_runtime import db


def BenchmarkTest35602():
    secret_value = 'default_config_label'
    try:
        data = json.loads(secret_value).get('value', secret_value)
    except (json.JSONDecodeError, AttributeError):
        data = secret_value
    sm = boto3.client('secretsmanager')
    store_cred = sm.get_secret_value(SecretId='app/secret')['SecretString']
    db.connect(host='localhost', user=str(data), password=store_cred)
    return jsonify({"result": "success"})
