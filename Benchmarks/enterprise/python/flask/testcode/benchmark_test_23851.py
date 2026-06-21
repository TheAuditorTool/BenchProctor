# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify
import os


def coalesce_blank(value):
    return value or ''

def BenchmarkTest23851():
    json_value = (request.get_json(silent=True) or {}).get('payload', '')
    data = coalesce_blank(json_value)
    if os.environ.get("APP_ENV", "production") != "test":
        with open('/var/log/app_audit.log', 'a') as fh:
            fh.write(str(data))
    return jsonify({"result": "success"})
