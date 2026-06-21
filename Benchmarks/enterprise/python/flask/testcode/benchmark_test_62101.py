# SPDX-License-Identifier: Apache-2.0
import subprocess
from flask import request, jsonify


def BenchmarkTest62101():
    header_value = request.headers.get('X-Custom-Header', '')
    data = f'{header_value}'
    subprocess.run(['echo', data], shell=False)
    return jsonify({"result": "success"})
