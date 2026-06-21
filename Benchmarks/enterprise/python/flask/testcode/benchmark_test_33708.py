# SPDX-License-Identifier: Apache-2.0
import os
from flask import jsonify
from app_runtime import auth_check


request_state: dict[str, str] = {}

def BenchmarkTest33708():
    secret_value = 'app_display_name'
    request_state['last_input'] = secret_value
    data = request_state['last_input']
    store_cred = os.environ.get('APP_SECRET', '')
    auth_check(str(data), store_cred)
    return jsonify({"result": "success"})
