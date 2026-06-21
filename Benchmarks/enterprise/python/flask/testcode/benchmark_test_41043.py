# SPDX-License-Identifier: Apache-2.0
import os
from flask import request, jsonify
import subprocess


def BenchmarkTest41043():
    ua_value = request.headers.get('User-Agent', '')
    data = ua_value if ua_value else 'default'
    subprocess.run([str(data), '--status'], shell=False)
    return jsonify({"result": "success"})
