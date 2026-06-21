# SPDX-License-Identifier: Apache-2.0
import os
from flask import request, jsonify
import subprocess


def BenchmarkTest04479():
    host_value = request.headers.get('Host', '')
    prefix = ''
    data = prefix + str(host_value)
    subprocess.run([str(data), '--status'], shell=False)
    return jsonify({"result": "success"})
