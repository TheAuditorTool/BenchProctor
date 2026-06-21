# SPDX-License-Identifier: Apache-2.0
import os
from flask import request, jsonify
from app_runtime import auth_check


def BenchmarkTest67512():
    host_value = request.headers.get('Host', '')
    store_cred = os.environ.get('APP_SECRET', '')
    auth_check(str(host_value), store_cred)
    return jsonify({"result": "success"})
