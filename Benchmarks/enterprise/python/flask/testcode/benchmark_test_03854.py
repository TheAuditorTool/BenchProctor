# SPDX-License-Identifier: Apache-2.0
import os
from flask import request, jsonify
import json
from app_runtime import auth_check


def BenchmarkTest03854():
    referer_value = request.headers.get('Referer', '')
    try:
        data = json.loads(referer_value).get('value', referer_value)
    except (json.JSONDecodeError, AttributeError):
        data = referer_value
    store_cred = os.environ.get('APP_SECRET', '')
    auth_check(str(data), store_cred)
    return jsonify({"result": "success"})
