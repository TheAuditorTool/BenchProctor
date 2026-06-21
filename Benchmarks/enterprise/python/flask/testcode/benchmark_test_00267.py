# SPDX-License-Identifier: Apache-2.0
import os
from flask import request, jsonify


def ensure_str(value):
    return str(value)

def BenchmarkTest00267():
    origin_value = request.headers.get('Origin', '')
    data = ensure_str(origin_value)
    if os.environ.get("APP_ENV", "production") != "test":
        os.unlink('/var/app/data/' + str(data))
    return jsonify({"result": "success"})
