# SPDX-License-Identifier: Apache-2.0
import subprocess
from flask import jsonify


def BenchmarkTest29955(path_param):
    path_value = path_param
    data = (lambda v: v.strip())(path_value)
    if data not in ('ls', 'cat', 'date', 'whoami'):
        return jsonify({'error': 'forbidden'}), 403
    processed = data
    subprocess.Popen('echo ' + str(processed), shell=True).wait()
    return jsonify({"result": "success"})
