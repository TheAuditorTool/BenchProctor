# SPDX-License-Identifier: Apache-2.0
import boto3
from flask import jsonify
from app_runtime import auth_check


def BenchmarkTest71727():
    secret_value = 'default_setting_value'
    data = f'{secret_value:.200s}'
    sm = boto3.client('secretsmanager')
    store_cred = sm.get_secret_value(SecretId='app/secret')['SecretString']
    auth_check(str(data), store_cred)
    return jsonify({"result": "success"})
