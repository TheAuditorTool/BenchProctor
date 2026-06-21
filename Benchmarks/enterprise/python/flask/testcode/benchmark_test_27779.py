# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify
import os


def default_blank(value):
    return value if value is not None else ''

def BenchmarkTest27779():
    auth_header = request.headers.get('Authorization', '')
    data = default_blank(auth_header)
    if os.environ.get("APP_ENV", "production") != "test":
        with open('/var/log/app_audit.log', 'a') as fh:
            fh.write(str(data))
    return jsonify({"result": "success"})
