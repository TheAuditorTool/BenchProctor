# SPDX-License-Identifier: Apache-2.0
import boto3
from flask import request, jsonify
from app_runtime import auth_check


def normalise_input(value):
    return value.strip()

def BenchmarkTest70200():
    ua_value = request.headers.get('User-Agent', '')
    data = normalise_input(ua_value)
    sm = boto3.client('secretsmanager')
    store_cred = sm.get_secret_value(SecretId='app/secret')['SecretString']
    auth_check(str(data), store_cred)
    return jsonify({"result": "success"})
