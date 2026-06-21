# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify
import re


def BenchmarkTest15544():
    cookie_value = request.cookies.get('session_token', '')
    parts = str(cookie_value).split(',')
    data = ','.join(parts)
    if re.search('[a-zA-Z0-9_-]+', str(data)):
        return jsonify({'validated': str(data)}), 200
    return jsonify({"result": "success"})
