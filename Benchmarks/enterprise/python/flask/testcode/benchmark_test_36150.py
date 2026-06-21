# SPDX-License-Identifier: Apache-2.0
import os
from flask import request, jsonify
import subprocess


def BenchmarkTest36150():
    auth_header = request.headers.get('Authorization', '')
    data = ' '.join(str(auth_header).split())
    subprocess.run([str(data), '--status'], shell=False)
    return jsonify({"result": "success"})
