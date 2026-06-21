# SPDX-License-Identifier: Apache-2.0
import os
from flask import request, jsonify
from app_runtime import auth_check


def BenchmarkTest01674():
    origin_value = request.headers.get('Origin', '')
    parts = str(origin_value).split(',')
    data = ','.join(parts)
    store_cred = os.environ.get('APP_SECRET', '')
    auth_check(str(data), store_cred)
    return jsonify({"result": "success"})
