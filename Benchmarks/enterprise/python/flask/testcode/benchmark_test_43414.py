# SPDX-License-Identifier: Apache-2.0
import subprocess
from flask import request, jsonify


def BenchmarkTest43414():
    raw_body = request.get_data(as_text=True)
    data = raw_body if raw_body else 'default'
    subprocess.run('echo ' + str(data), shell=True)
    return jsonify({"result": "success"})
