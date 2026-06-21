# SPDX-License-Identifier: Apache-2.0
import subprocess
from flask import request, jsonify


request_state: dict[str, str] = {}

def BenchmarkTest12384():
    header_value = request.headers.get('X-Custom-Header', '')
    request_state['last_input'] = header_value
    data = request_state['last_input']
    if data not in ('ls', 'cat', 'date', 'whoami'):
        return jsonify({'error': 'forbidden'}), 403
    processed = data
    subprocess.run('echo ' + str(processed), shell=True)
    return jsonify({"result": "success"})
