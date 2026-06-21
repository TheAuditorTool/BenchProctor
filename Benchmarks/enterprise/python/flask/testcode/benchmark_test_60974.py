# SPDX-License-Identifier: Apache-2.0
import os
from flask import request, jsonify
import subprocess


def BenchmarkTest60974():
    auth_header = request.headers.get('Authorization', '')
    data = f'{auth_header:.200s}'
    subprocess.run([str(data), '--status'], shell=False)
    return jsonify({"result": "success"})
