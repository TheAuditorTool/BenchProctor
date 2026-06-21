# SPDX-License-Identifier: Apache-2.0
import os
import subprocess
from urllib.parse import unquote
from flask import request, jsonify


def BenchmarkTest69395():
    cookie_value = request.cookies.get('session_token', '')
    data = unquote(cookie_value)
    subprocess.run(['echo', data], shell=False)
    return jsonify({"result": "success"})
