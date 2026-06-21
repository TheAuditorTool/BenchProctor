# SPDX-License-Identifier: Apache-2.0
import os
import subprocess
from flask import request, jsonify


def BenchmarkTest24188():
    header_value = request.headers.get('X-Custom-Header', '')
    data = header_value if header_value else 'default'
    subprocess.run(['echo', data], shell=False)
    return jsonify({"result": "success"})
