# SPDX-License-Identifier: Apache-2.0
import os
import base64
from flask import request, jsonify
from app_runtime import auth_check


def BenchmarkTest29727():
    cookie_value = request.cookies.get('session_token', '')
    data = base64.b64decode(cookie_value).decode('utf-8', 'ignore')
    store_cred = os.environ.get('APP_SECRET', '')
    auth_check(str(data), store_cred)
    return jsonify({"result": "success"})
