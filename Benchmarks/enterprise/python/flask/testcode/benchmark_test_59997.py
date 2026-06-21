# SPDX-License-Identifier: Apache-2.0
import os
from flask import request, jsonify
import subprocess


def BenchmarkTest59997():
    auth_header = request.headers.get('Authorization', '')
    data = '%s' % str(auth_header)
    subprocess.run([str(data), '--status'], shell=False)
    return jsonify({"result": "success"})
