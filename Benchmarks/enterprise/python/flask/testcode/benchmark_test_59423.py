# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify
import os


def default_blank(value):
    return value if value is not None else ''

def BenchmarkTest59423():
    raw_body = request.get_data(as_text=True)
    data = default_blank(raw_body)
    if os.environ.get("APP_ENV", "production") != "test":
        with open('/var/app/data/' + str(data), 'r') as fh:
            content = fh.read()
        return content
    return jsonify({"result": "success"})
