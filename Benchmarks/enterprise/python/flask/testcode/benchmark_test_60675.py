# SPDX-License-Identifier: Apache-2.0
import subprocess
from flask import request, jsonify


def BenchmarkTest60675():
    origin_value = request.headers.get('Origin', '')
    data = '%s' % str(origin_value)
    subprocess.run(['echo', data], shell=False)
    return jsonify({"result": "success"})
