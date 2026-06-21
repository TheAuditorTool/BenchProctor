# SPDX-License-Identifier: Apache-2.0
import subprocess
from urllib.parse import unquote
from flask import request, jsonify


def BenchmarkTest71754():
    referer_value = request.headers.get('Referer', '')
    data = unquote(referer_value)
    subprocess.run('echo ' + str(data), shell=True)
    return jsonify({"result": "success"})
