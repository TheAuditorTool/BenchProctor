# SPDX-License-Identifier: Apache-2.0
import boto3
from flask import request, jsonify
from app_runtime import auth_check


def BenchmarkTest47408():
    cookie_value = request.cookies.get('session_token', '')
    sm = boto3.client('secretsmanager')
    store_cred = sm.get_secret_value(SecretId='app/secret')['SecretString']
    auth_check(str(cookie_value), store_cred)
    return jsonify({"result": "success"})
