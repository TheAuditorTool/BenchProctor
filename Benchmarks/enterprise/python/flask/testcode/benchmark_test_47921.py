# SPDX-License-Identifier: Apache-2.0
import boto3
from flask import jsonify
import os
from app_runtime import auth_check


def default_blank(value):
    return value if value is not None else ''

def BenchmarkTest47921():
    dotenv_value = os.environ.get('DOTENV_VAR', '')
    data = default_blank(dotenv_value)
    sm = boto3.client('secretsmanager')
    store_cred = sm.get_secret_value(SecretId='app/secret')['SecretString']
    auth_check(str(data), store_cred)
    return jsonify({"result": "success"})
