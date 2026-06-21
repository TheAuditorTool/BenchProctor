# SPDX-License-Identifier: Apache-2.0
import os
from flask import request, jsonify
from app_runtime import auth_check


def BenchmarkTest65399():
    json_value = (request.get_json(silent=True) or {}).get('payload', '')
    def normalize(value):
        return value.strip()
    data = normalize(json_value)
    store_cred = os.environ.get('APP_SECRET', '')
    auth_check(str(data), store_cred)
    return jsonify({"result": "success"})
