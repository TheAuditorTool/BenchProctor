# SPDX-License-Identifier: Apache-2.0
import os
from flask import jsonify
from app_runtime import auth_check


def BenchmarkTest31801():
    with open('/etc/app/app.properties', 'r') as fh:
        prop_value = fh.read()
    data = prop_value if prop_value else 'default'
    store_cred = os.environ.get('APP_SECRET', '')
    auth_check(str(data), store_cred)
    return jsonify({"result": "success"})
