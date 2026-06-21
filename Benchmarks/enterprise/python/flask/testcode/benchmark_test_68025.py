# SPDX-License-Identifier: Apache-2.0
import tempfile
from flask import request, jsonify
import os


request_state: dict[str, str] = {}

def BenchmarkTest68025():
    user_id = request.args.get('id', '')
    request_state['last_input'] = user_id
    data = request_state['last_input']
    fd, path = tempfile.mkstemp(prefix='upload_', dir='/var/app/tmp')
    with os.fdopen(fd, 'w') as fh:
        fh.write(str(data))
    return jsonify({"result": "success"})
