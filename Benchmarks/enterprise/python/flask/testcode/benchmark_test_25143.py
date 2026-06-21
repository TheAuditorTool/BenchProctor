# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify
import os


def ensure_str(value):
    return str(value)

def BenchmarkTest25143():
    host_value = request.headers.get('Host', '')
    data = ensure_str(host_value)
    if os.environ.get("APP_ENV", "production") != "test":
        with open('/var/log/app_audit.log', 'a') as fh:
            fh.write(str(data))
    return jsonify({"result": "success"})
