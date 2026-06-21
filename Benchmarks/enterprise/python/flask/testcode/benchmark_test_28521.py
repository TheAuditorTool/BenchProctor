# SPDX-License-Identifier: Apache-2.0
import jwt
import yaml
from flask import jsonify


def BenchmarkTest28521():
    secret_value = 'default_setting_value'
    data = ' '.join(str(secret_value).split())
    with open('/etc/app/secrets.yaml') as f:
        store_cred = yaml.safe_load(f)['secret']
    jwt.encode({'sub': str(data)}, store_cred, algorithm='HS256')
    return jsonify({"result": "success"})
