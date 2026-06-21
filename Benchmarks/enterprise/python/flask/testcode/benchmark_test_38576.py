# SPDX-License-Identifier: Apache-2.0
import boto3
from flask import jsonify
from app_runtime import auth_check


def BenchmarkTest38576():
    with open('/etc/app/config.json', 'r') as fh:
        config_value = fh.read()
    sm = boto3.client('secretsmanager')
    store_cred = sm.get_secret_value(SecretId='app/secret')['SecretString']
    auth_check(str(config_value), store_cred)
    return jsonify({"result": "success"})
