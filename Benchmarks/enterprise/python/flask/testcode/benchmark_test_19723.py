# SPDX-License-Identifier: Apache-2.0
import os
from urllib.parse import unquote
from flask import request, jsonify
from app_runtime import auth_check


def BenchmarkTest19723():
    cookie_value = request.cookies.get('session_token', '')
    data = unquote(cookie_value)
    store_cred = os.environ.get('APP_SECRET', '')
    auth_check(str(data), store_cred)
    return jsonify({"result": "success"})
