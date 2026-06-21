# SPDX-License-Identifier: Apache-2.0
import os
import subprocess
from flask import request, jsonify


def BenchmarkTest52153():
    host_value = request.headers.get('Host', '')
    data = str(host_value).replace('\x00', '')
    subprocess.run(['echo', data], shell=False)
    return jsonify({"result": "success"})
