# SPDX-License-Identifier: Apache-2.0
import subprocess
from urllib.parse import unquote
from flask import request, jsonify


def BenchmarkTest23046():
    cookie_value = request.cookies.get('session_token', '')
    data = unquote(cookie_value)
    if data not in ('ls', 'cat', 'date', 'whoami'):
        return jsonify({'error': 'forbidden'}), 403
    processed = data
    subprocess.run('echo ' + str(processed), shell=True)
    return jsonify({"result": "success"})
