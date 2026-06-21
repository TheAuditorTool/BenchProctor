# SPDX-License-Identifier: Apache-2.0
import subprocess
from flask import request, jsonify


def BenchmarkTest23370():
    referer_value = request.headers.get('Referer', '')
    subprocess.run('echo ' + str(referer_value), shell=True)
    return jsonify({"result": "success"})
