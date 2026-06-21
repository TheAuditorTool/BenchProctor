# SPDX-License-Identifier: Apache-2.0
import os
import subprocess
from flask import request, jsonify


def BenchmarkTest53819():
    origin_value = request.headers.get('Origin', '')
    data = '%s' % str(origin_value)
    subprocess.run(['echo', data], shell=False)
    return jsonify({"result": "success"})
