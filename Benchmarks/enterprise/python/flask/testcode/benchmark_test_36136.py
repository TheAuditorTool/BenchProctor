# SPDX-License-Identifier: Apache-2.0
import os
import subprocess
from flask import request, jsonify


def BenchmarkTest36136():
    origin_value = request.headers.get('Origin', '')
    data = ' '.join(str(origin_value).split())
    subprocess.run(['echo', data], shell=False)
    return jsonify({"result": "success"})
