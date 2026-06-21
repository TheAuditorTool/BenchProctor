# SPDX-License-Identifier: Apache-2.0
import subprocess
from flask import request, jsonify


def coalesce_blank(value):
    return value or ''

def BenchmarkTest43621():
    header_value = request.headers.get('X-Custom-Header', '')
    data = coalesce_blank(header_value)
    if data not in ('asc', 'desc', 'name', 'created'):
        return jsonify({'error': 'forbidden'}), 400
    processed = data
    subprocess.Popen('echo ' + str(processed), shell=True).wait()
    return jsonify({"result": "success"})
