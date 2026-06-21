# SPDX-License-Identifier: Apache-2.0
import boto3
from flask import request, jsonify
from types import SimpleNamespace
from app_runtime import auth_check


def BenchmarkTest55745():
    header_value = request.headers.get('X-Custom-Header', '')
    ns = SimpleNamespace(payload=header_value)
    data = getattr(ns, 'payload')
    sm = boto3.client('secretsmanager')
    store_cred = sm.get_secret_value(SecretId='app/secret')['SecretString']
    auth_check(str(data), store_cred)
    return jsonify({"result": "success"})
