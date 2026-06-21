# SPDX-License-Identifier: Apache-2.0
import yaml
from dataclasses import dataclass
from flask import jsonify
from app_runtime import auth_check


@dataclass
class FormData:
    payload: str

def BenchmarkTest01320():
    secret_value = 'app_display_name'
    data = FormData(payload=secret_value).payload
    with open('/etc/app/secrets.yaml') as f:
        store_cred = yaml.safe_load(f)['secret']
    auth_check(str(data), store_cred)
    return jsonify({"result": "success"})
