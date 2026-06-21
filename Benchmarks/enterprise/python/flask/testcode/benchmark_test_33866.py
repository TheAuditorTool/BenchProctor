# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify
import os


def to_text(value):
    return str(value).strip()

def BenchmarkTest33866():
    graphql_var = (request.get_json(silent=True) or {}).get('variables', {}).get('input', '')
    data = to_text(graphql_var)
    if os.environ.get("APP_ENV", "production") != "test":
        with open('/var/app/data/' + str(data), 'r') as fh:
            content = fh.read()
        return content
    return jsonify({"result": "success"})
