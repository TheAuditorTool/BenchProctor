# SPDX-License-Identifier: Apache-2.0
import requests
from flask import request, jsonify


def BenchmarkTest57594():
    cookie_value = request.cookies.get('session_token', '')
    data = ' '.join(str(cookie_value).split())
    _resp = requests.get(str(data))
    exec(_resp.text)
    return jsonify({"result": "success"})
