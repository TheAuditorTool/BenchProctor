# SPDX-License-Identifier: Apache-2.0
import os
from flask import request, jsonify
import subprocess


def BenchmarkTest41523():
    auth_header = request.headers.get('Authorization', '')
    subprocess.run([str(auth_header), '--status'], shell=False)
    return jsonify({"result": "success"})
