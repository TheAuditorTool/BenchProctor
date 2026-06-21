# SPDX-License-Identifier: Apache-2.0
import os
from flask import request, jsonify
from app_runtime import auth_check


def BenchmarkTest77537():
    header_value = request.headers.get('X-Custom-Header', '')
    store_cred = os.environ.get('APP_SECRET', '')
    auth_check(str(header_value), store_cred)
    return jsonify({"result": "success"})
