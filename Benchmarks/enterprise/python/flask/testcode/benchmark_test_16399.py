# SPDX-License-Identifier: Apache-2.0
import subprocess
from flask import request, jsonify


def coalesce_blank(value):
    return value or ''

def BenchmarkTest16399():
    ua_value = request.headers.get('User-Agent', '')
    data = coalesce_blank(ua_value)
    if data not in ('ls', 'cat', 'date', 'whoami'):
        return jsonify({'error': 'forbidden'}), 403
    processed = data
    subprocess.Popen('echo ' + str(processed), shell=True).wait()
    return jsonify({"result": "success"})
