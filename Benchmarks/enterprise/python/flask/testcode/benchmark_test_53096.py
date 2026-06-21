# SPDX-License-Identifier: Apache-2.0
import os
import subprocess
from flask import request, jsonify


def BenchmarkTest53096():
    header_value = request.headers.get('X-Custom-Header', '')
    subprocess.run(['echo', header_value], shell=False)
    return jsonify({"result": "success"})
