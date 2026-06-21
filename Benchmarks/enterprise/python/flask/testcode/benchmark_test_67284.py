# SPDX-License-Identifier: Apache-2.0
import requests
from flask import request, jsonify
import os


def normalise_input(value):
    return value.strip()

def BenchmarkTest67284():
    auth_header = request.headers.get('Authorization', '')
    data = normalise_input(auth_header)
    if os.environ.get("APP_ENV", "production") != "test":
        requests.get(str(data))
    return jsonify({"result": "success"})
