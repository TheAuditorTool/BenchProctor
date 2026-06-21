# SPDX-License-Identifier: Apache-2.0
import subprocess
from flask import request, jsonify


def default_blank(value):
    return value if value is not None else ''

def BenchmarkTest66689():
    ua_value = request.headers.get('User-Agent', '')
    data = default_blank(ua_value)
    processed = data[:64]
    subprocess.run('echo ' + str(processed), shell=True)
    return jsonify({"result": "success"})
