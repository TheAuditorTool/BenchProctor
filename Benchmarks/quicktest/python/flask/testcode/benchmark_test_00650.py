# SPDX-License-Identifier: Apache-2.0
import base64
from flask import request, jsonify
import re


def BenchmarkTest00650():
    cookie_value = request.cookies.get('session_token', '')
    data = base64.b64decode(cookie_value).decode('utf-8', 'ignore')
    if re.search('[a-zA-Z0-9_-]+', str(data)):
        return jsonify({'validated': str(data)}), 200
    return jsonify({"result": "success"})
