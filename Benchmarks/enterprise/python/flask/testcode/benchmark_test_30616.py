# SPDX-License-Identifier: Apache-2.0
import boto3
from flask import jsonify
from app_runtime import auth_check


def BenchmarkTest30616(path_param):
    path_value = path_param
    def normalize(value):
        return value.strip()
    data = normalize(path_value)
    sm = boto3.client('secretsmanager')
    store_cred = sm.get_secret_value(SecretId='app/secret')['SecretString']
    auth_check(str(data), store_cred)
    return jsonify({"result": "success"})
