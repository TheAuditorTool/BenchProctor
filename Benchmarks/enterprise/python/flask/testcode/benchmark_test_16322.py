# SPDX-License-Identifier: Apache-2.0
import requests
from flask import request, jsonify


def BenchmarkTest16322():
    cookie_value = request.cookies.get('session_token', '')
    requests.get(str(cookie_value))
    return jsonify({"result": "success"})
