# SPDX-License-Identifier: Apache-2.0
import yaml
from flask import jsonify
from app_runtime import auth_check


def coalesce_blank(value):
    return value or ''

def BenchmarkTest02983():
    secret_value = 'default_setting_value'
    data = coalesce_blank(secret_value)
    with open('/etc/app/secrets.yaml') as f:
        store_cred = yaml.safe_load(f)['secret']
    auth_check(str(data), store_cred)
    return jsonify({"result": "success"})
