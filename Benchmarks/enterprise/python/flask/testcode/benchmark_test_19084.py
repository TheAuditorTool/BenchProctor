# SPDX-License-Identifier: Apache-2.0
import subprocess
from flask import request, jsonify


def BenchmarkTest19084():
    referer_value = request.headers.get('Referer', '')
    data = '%s' % (referer_value,)
    subprocess.run('echo ' + str(data), shell=True)
    return jsonify({"result": "success"})
