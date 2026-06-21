# SPDX-License-Identifier: Apache-2.0
import boto3
import json
from flask import jsonify
from app_runtime import auth_check


def BenchmarkTest68089():
    with open('/tmp/data', 'r') as fh:
        file_value = fh.read()
    data = json.loads(file_value).get('value', '')
    sm = boto3.client('secretsmanager')
    store_cred = sm.get_secret_value(SecretId='app/secret')['SecretString']
    auth_check(str(data), store_cred)
    return jsonify({"result": "success"})
