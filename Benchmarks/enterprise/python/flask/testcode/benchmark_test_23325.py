# SPDX-License-Identifier: Apache-2.0
import os
from dataclasses import dataclass
from flask import jsonify
from app_runtime import auth_check


@dataclass
class FormData:
    payload: str

def BenchmarkTest23325():
    secret_value = 'default_config_label'
    data = FormData(payload=secret_value).payload
    store_cred = os.environ.get('APP_SECRET', '')
    auth_check(str(data), store_cred)
    return jsonify({"result": "success"})
