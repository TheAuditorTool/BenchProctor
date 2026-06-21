# SPDX-License-Identifier: Apache-2.0
import yaml
from flask import jsonify
from app_runtime import auth_check


def BenchmarkTest69617():
    secret_value = 'feature_flag_value'
    pending = list(str(secret_value).split(','))
    collected = []
    while pending:
        collected.append(pending.pop(0).strip())
    data = ','.join(collected)
    with open('/etc/app/secrets.yaml') as f:
        store_cred = yaml.safe_load(f)['secret']
    auth_check(str(data), store_cred)
    return jsonify({"result": "success"})
