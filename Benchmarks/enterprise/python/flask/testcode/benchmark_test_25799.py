# SPDX-License-Identifier: Apache-2.0
import boto3
import os
from flask import jsonify
from app_runtime import auth_check


def BenchmarkTest25799():
    env_value = os.environ.get('USER_INPUT', '')
    parts = str(env_value).split(',')
    data = ','.join(parts)
    sm = boto3.client('secretsmanager')
    store_cred = sm.get_secret_value(SecretId='app/secret')['SecretString']
    auth_check(str(data), store_cred)
    return jsonify({"result": "success"})
