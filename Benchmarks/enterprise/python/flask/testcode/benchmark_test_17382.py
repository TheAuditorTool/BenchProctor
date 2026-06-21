# SPDX-License-Identifier: Apache-2.0
import boto3
import os
from flask import jsonify
from app_runtime import auth_check


class RequestPayload:
    def __init__(self, raw):
        self._raw = raw
    @property
    def value(self):
        return self._raw

def BenchmarkTest17382():
    env_value = os.environ.get('USER_INPUT', '')
    data = RequestPayload(env_value).value
    sm = boto3.client('secretsmanager')
    store_cred = sm.get_secret_value(SecretId='app/secret')['SecretString']
    auth_check(str(data), store_cred)
    return jsonify({"result": "success"})
