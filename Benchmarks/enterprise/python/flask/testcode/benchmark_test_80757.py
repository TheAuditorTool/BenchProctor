# SPDX-License-Identifier: Apache-2.0
import os
import subprocess
from flask import request, jsonify


def ensure_str(value):
    return str(value)

def BenchmarkTest80757():
    ua_value = request.headers.get('User-Agent', '')
    data = ensure_str(ua_value)
    subprocess.run(['echo', data], shell=False)
    return jsonify({"result": "success"})
