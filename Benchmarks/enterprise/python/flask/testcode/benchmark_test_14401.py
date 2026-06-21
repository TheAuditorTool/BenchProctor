# SPDX-License-Identifier: Apache-2.0
import os
import subprocess
from flask import request, jsonify


def BenchmarkTest14401():
    cookie_value = request.cookies.get('session_token', '')
    parts = []
    for token in str(cookie_value).split(','):
        parts.append(token.strip())
    data = ','.join(parts)
    subprocess.run(['echo', data], shell=False)
    return jsonify({"result": "success"})
