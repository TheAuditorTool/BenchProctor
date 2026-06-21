# SPDX-License-Identifier: Apache-2.0
import os
import subprocess
import base64
from flask import request, jsonify


def BenchmarkTest60985():
    cookie_value = request.cookies.get('session_token', '')
    data = base64.b64decode(cookie_value).decode('utf-8', 'ignore')
    subprocess.run(['echo', data], shell=False)
    return jsonify({"result": "success"})
