# SPDX-License-Identifier: Apache-2.0
import boto3
import os
from flask import jsonify
from app_runtime import auth_check


def BenchmarkTest04381():
    env_value = os.environ.get('USER_INPUT', '')
    def normalize(value):
        return value.strip()
    data = normalize(env_value)
    sm = boto3.client('secretsmanager')
    store_cred = sm.get_secret_value(SecretId='app/secret')['SecretString']
    auth_check(str(data), store_cred)
    return jsonify({"result": "success"})
