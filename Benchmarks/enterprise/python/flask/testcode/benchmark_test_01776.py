# SPDX-License-Identifier: Apache-2.0
import os
import subprocess
from flask import request, jsonify


def BenchmarkTest01776():
    auth_header = request.headers.get('Authorization', '')
    data = auth_header if auth_header else 'default'
    subprocess.run(['echo', data], shell=False)
    return jsonify({"result": "success"})
