# SPDX-License-Identifier: Apache-2.0
import os
from flask import request, jsonify
import subprocess


def BenchmarkTest27466():
    header_value = request.headers.get('X-Custom-Header', '')
    data = f'{header_value:.200s}'
    subprocess.run([str(data), '--status'], shell=False)
    return jsonify({"result": "success"})
