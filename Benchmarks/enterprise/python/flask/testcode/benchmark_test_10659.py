# SPDX-License-Identifier: Apache-2.0
import os
from flask import request, jsonify
import subprocess


def BenchmarkTest10659():
    host_value = request.headers.get('Host', '')
    data = f'{host_value:.200s}'
    subprocess.run([str(data), '--status'], shell=False)
    return jsonify({"result": "success"})
