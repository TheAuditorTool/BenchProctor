# SPDX-License-Identifier: Apache-2.0
import subprocess
import re
from flask import jsonify


def BenchmarkTest25229(path_param):
    path_value = path_param
    data = path_value if path_value else 'default'
    if not re.fullmatch(r'^[a-zA-Z0-9_.-]+$', str(data)):
        return jsonify({'error': 'invalid input'}), 400
    processed = data
    subprocess.Popen('echo ' + str(processed), shell=True).wait()
    return jsonify({"result": "success"})
