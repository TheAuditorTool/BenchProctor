# SPDX-License-Identifier: Apache-2.0
import boto3
from flask import jsonify
import os
from app_runtime import auth_check


def BenchmarkTest51115():
    dotenv_value = os.environ.get('DOTENV_VAR', '')
    sm = boto3.client('secretsmanager')
    store_cred = sm.get_secret_value(SecretId='app/secret')['SecretString']
    auth_check(str(dotenv_value), store_cred)
    return jsonify({"result": "success"})
