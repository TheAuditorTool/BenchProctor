# SPDX-License-Identifier: Apache-2.0
import os
from flask import request, jsonify
from app_runtime import auth_check


def BenchmarkTest18645():
    auth_header = request.headers.get('Authorization', '')
    data = auth_header if auth_header else 'default'
    store_cred = os.environ.get('APP_SECRET', '')
    auth_check(str(data), store_cred)
    return jsonify({"result": "success"})
