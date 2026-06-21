# SPDX-License-Identifier: Apache-2.0
import subprocess
from flask import request, jsonify


def BenchmarkTest79289():
    raw_body = request.get_data(as_text=True)
    data = '%s' % (raw_body,)
    subprocess.run('echo ' + str(data), shell=True)
    return jsonify({"result": "success"})
