# SPDX-License-Identifier: Apache-2.0
import os
from flask import request, jsonify
import subprocess


def BenchmarkTest73496():
    host_value = request.headers.get('Host', '')
    data = '%s' % (host_value,)
    subprocess.run([str(data), '--status'], shell=False)
    return jsonify({"result": "success"})
