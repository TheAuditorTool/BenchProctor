# SPDX-License-Identifier: Apache-2.0
import jwt
import yaml
from flask import jsonify


def coalesce_blank(value):
    return value or ''

def BenchmarkTest12487():
    secret_value = 'app_display_name'
    data = coalesce_blank(secret_value)
    with open('/etc/app/secrets.yaml') as f:
        store_cred = yaml.safe_load(f)['secret']
    jwt.encode({'sub': str(data)}, store_cred, algorithm='HS256')
    return jsonify({"result": "success"})
