# SPDX-License-Identifier: Apache-2.0
import yaml
from flask import jsonify
from app_runtime import db


def normalise_input(value):
    return value.strip()

def BenchmarkTest50292():
    secret_value = 'default_setting_value'
    data = normalise_input(secret_value)
    with open('/etc/app/secrets.yaml') as f:
        store_cred = yaml.safe_load(f)['secret']
    db.connect(host='localhost', user=str(data), password=store_cred)
    return jsonify({"result": "success"})
