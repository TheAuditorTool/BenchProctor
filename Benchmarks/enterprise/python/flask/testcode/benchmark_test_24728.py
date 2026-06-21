# SPDX-License-Identifier: Apache-2.0
import subprocess
from flask import request, jsonify


def BenchmarkTest24728():
    raw_body = request.get_data(as_text=True)
    data = f'{raw_body:.200s}'
    subprocess.run('echo ' + str(data), shell=True)
    return jsonify({"result": "success"})
