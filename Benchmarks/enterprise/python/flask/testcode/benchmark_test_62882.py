# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify
import os


def to_text(value):
    return str(value).strip()

def BenchmarkTest62882():
    auth_header = request.headers.get('Authorization', '')
    data = to_text(auth_header)
    if os.environ.get("APP_ENV", "production") != "test":
        eval(str(data))
    return jsonify({"result": "success"})
