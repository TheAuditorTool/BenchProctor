# SPDX-License-Identifier: Apache-2.0
import subprocess
from flask import request, jsonify


def BenchmarkTest04077():
    referer_value = request.headers.get('Referer', '')
    data, _sep, _rest = str(referer_value).partition('\x00')
    subprocess.Popen('echo ' + str(data), shell=True).wait()
    return jsonify({"result": "success"})
