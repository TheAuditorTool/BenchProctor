# SPDX-License-Identifier: Apache-2.0
import os
from flask import jsonify
from app_runtime import auth_check


def BenchmarkTest75863():
    with open('/tmp/data', 'r') as fh:
        file_value = fh.read()
    if file_value:
        data = file_value
    else:
        data = ''
    store_cred = os.environ.get('APP_SECRET', '')
    auth_check(str(data), store_cred)
    return jsonify({"result": "success"})
