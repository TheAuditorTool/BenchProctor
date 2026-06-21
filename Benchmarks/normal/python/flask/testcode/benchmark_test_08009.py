# SPDX-License-Identifier: Apache-2.0
import yaml
from flask import jsonify
from app_runtime import db


def BenchmarkTest08009():
    secret_value = 'app_display_name'
    with open('/etc/app/secrets.yaml') as f:
        store_cred = yaml.safe_load(f)['secret']
    db.connect(host='localhost', user=str(secret_value), password=store_cred)
    return jsonify({"result": "success"})
