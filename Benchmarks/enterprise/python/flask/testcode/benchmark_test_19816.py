# SPDX-License-Identifier: Apache-2.0
import os
import subprocess
from flask import request, jsonify


def BenchmarkTest19816():
    host_value = request.headers.get('Host', '')
    data = '%s' % (host_value,)
    subprocess.run(['echo', data], shell=False)
    return jsonify({"result": "success"})
