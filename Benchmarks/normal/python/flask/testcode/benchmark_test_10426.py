# SPDX-License-Identifier: Apache-2.0
import yaml
from flask import jsonify
from app_runtime import auth_check


def BenchmarkTest10426():
    secret_value = 'default_config_label'
    data = f'{secret_value:.200s}'
    with open('/etc/app/secrets.yaml') as f:
        store_cred = yaml.safe_load(f)['secret']
    auth_check(str(data), store_cred)
    return jsonify({"result": "success"})
