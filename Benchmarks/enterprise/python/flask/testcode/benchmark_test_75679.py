# SPDX-License-Identifier: Apache-2.0
import boto3
from flask import jsonify
from types import SimpleNamespace
from app_runtime import auth_check


def BenchmarkTest75679():
    secret_value = 'default_config_label'
    ns = SimpleNamespace(payload=secret_value)
    data = getattr(ns, 'payload')
    sm = boto3.client('secretsmanager')
    store_cred = sm.get_secret_value(SecretId='app/secret')['SecretString']
    auth_check(str(data), store_cred)
    return jsonify({"result": "success"})
