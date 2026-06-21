# SPDX-License-Identifier: Apache-2.0
import os
import subprocess
from flask import request, jsonify


def BenchmarkTest27727():
    header_value = request.headers.get('X-Custom-Header', '')
    data = '%s' % (header_value,)
    subprocess.run(['echo', data], shell=False)
    return jsonify({"result": "success"})
