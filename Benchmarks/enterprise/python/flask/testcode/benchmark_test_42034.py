# SPDX-License-Identifier: Apache-2.0
import tempfile
from flask import jsonify
import os


request_state: dict[str, str] = {}

def BenchmarkTest42034(path_param):
    path_value = path_param
    request_state['last_input'] = path_value
    data = request_state['last_input']
    fd, path = tempfile.mkstemp(prefix='upload_', dir='/var/app/tmp')
    with os.fdopen(fd, 'w') as fh:
        fh.write(str(data))
    return jsonify({"result": "success"})
