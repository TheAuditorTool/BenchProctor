# SPDX-License-Identifier: Apache-2.0
import subprocess
import re
from flask import request, jsonify


def BenchmarkTest06743():
    referer_value = request.headers.get('Referer', '')
    if not re.fullmatch(r'^[a-zA-Z0-9_.-]+$', str(referer_value)):
        return jsonify({'error': 'invalid input'}), 400
    processed = referer_value
    subprocess.Popen('echo ' + str(processed), shell=True).wait()
    return jsonify({"result": "success"})
