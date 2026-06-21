# SPDX-License-Identifier: Apache-2.0
import yaml
from flask import jsonify
import json
from app_runtime import db


def BenchmarkTest56973():
    secret_value = 'default_setting_value'
    try:
        data = json.loads(secret_value).get('value', secret_value)
    except (json.JSONDecodeError, AttributeError):
        data = secret_value
    with open('/etc/app/secrets.yaml') as f:
        store_cred = yaml.safe_load(f)['secret']
    db.connect(host='localhost', user=str(data), password=store_cred)
    return jsonify({"result": "success"})
