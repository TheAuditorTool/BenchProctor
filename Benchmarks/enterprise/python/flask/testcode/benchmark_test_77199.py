# SPDX-License-Identifier: Apache-2.0
import os
from flask import request, jsonify
import subprocess


def BenchmarkTest77199():
    header_value = request.headers.get('X-Custom-Header', '')
    data = '%s' % str(header_value)
    subprocess.run([str(data), '--status'], shell=False)
    return jsonify({"result": "success"})
