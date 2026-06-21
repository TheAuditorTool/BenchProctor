# SPDX-License-Identifier: Apache-2.0
import os
import subprocess
from flask import request, jsonify


def BenchmarkTest55029():
    auth_header = request.headers.get('Authorization', '')
    data = '%s' % str(auth_header)
    subprocess.run(['echo', data], shell=False)
    return jsonify({"result": "success"})
