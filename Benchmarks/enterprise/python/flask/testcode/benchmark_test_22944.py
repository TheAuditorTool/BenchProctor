# SPDX-License-Identifier: Apache-2.0
import os
import subprocess
from flask import request, jsonify


def BenchmarkTest22944():
    cookie_value = request.cookies.get('session_token', '')
    if cookie_value:
        data = cookie_value
    else:
        data = ''
    subprocess.run(['echo', data], shell=False)
    return jsonify({"result": "success"})
