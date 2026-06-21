# SPDX-License-Identifier: Apache-2.0
import os
from flask import request, jsonify
import subprocess


def BenchmarkTest04924():
    origin_value = request.headers.get('Origin', '')
    data = ' '.join(str(origin_value).split())
    subprocess.run([str(data), '--status'], shell=False)
    return jsonify({"result": "success"})
