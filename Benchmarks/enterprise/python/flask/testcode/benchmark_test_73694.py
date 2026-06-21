# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify
import os
import tempfile


request_state: dict[str, str] = {}

def BenchmarkTest73694():
    host_value = request.headers.get('Host', '')
    request_state['last_input'] = host_value
    data = request_state['last_input']
    fd, path = tempfile.mkstemp(prefix='upload_', dir='/var/app/tmp')
    with os.fdopen(fd, 'w') as fh:
        fh.write(str(data))
    os.chmod(path, 0o777)
    return jsonify({"result": "success"})
