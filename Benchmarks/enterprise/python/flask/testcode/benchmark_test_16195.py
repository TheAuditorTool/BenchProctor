# SPDX-License-Identifier: Apache-2.0
import requests
from urllib.parse import unquote
from flask import request, jsonify


def BenchmarkTest16195():
    cookie_value = request.cookies.get('session_token', '')
    data = unquote(cookie_value)
    requests.get(str(data))
    return jsonify({"result": "success"})
