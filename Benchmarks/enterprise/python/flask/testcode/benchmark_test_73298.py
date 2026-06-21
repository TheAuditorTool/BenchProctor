# SPDX-License-Identifier: Apache-2.0
import subprocess
import re
from urllib.parse import unquote
from flask import request, jsonify


def BenchmarkTest73298():
    referer_value = request.headers.get('Referer', '')
    data = unquote(referer_value)
    if not re.fullmatch(r'^[a-zA-Z0-9_-]+$', data):
        return jsonify({'error': 'forbidden'}), 400
    processed = data
    subprocess.Popen('echo ' + str(processed), shell=True).wait()
    return jsonify({"result": "success"})
