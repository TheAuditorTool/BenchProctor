# SPDX-License-Identifier: Apache-2.0
import os
from flask import request, jsonify
import subprocess


def BenchmarkTest31110():
    header_value = request.headers.get('X-Custom-Header', '')
    subprocess.run([str(header_value), '--status'], shell=False)
    return jsonify({"result": "success"})
