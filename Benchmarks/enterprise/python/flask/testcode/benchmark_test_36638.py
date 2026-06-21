# SPDX-License-Identifier: Apache-2.0
import os
import json
from flask import request, jsonify
from app_runtime import auth_check


def BenchmarkTest36638():
    raw_body = request.get_data(as_text=True)
    data = json.loads(raw_body).get('value', '')
    store_cred = os.environ.get('APP_SECRET', '')
    auth_check(str(data), store_cred)
    return jsonify({"result": "success"})
