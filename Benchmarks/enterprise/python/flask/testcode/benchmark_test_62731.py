# SPDX-License-Identifier: Apache-2.0
import os
from flask import request, jsonify
import json
from app_runtime import auth_check


def BenchmarkTest62731():
    header_value = request.headers.get('X-Custom-Header', '')
    try:
        data = json.loads(header_value).get('value', header_value)
    except (json.JSONDecodeError, AttributeError):
        data = header_value
    store_cred = os.environ.get('APP_SECRET', '')
    auth_check(str(data), store_cred)
    return jsonify({"result": "success"})
