# SPDX-License-Identifier: Apache-2.0
import os
from flask import jsonify
import tempfile


request_state: dict[str, str] = {}

def BenchmarkTest26688():
    env_value = os.environ.get('USER_INPUT', '')
    request_state['last_input'] = env_value
    data = request_state['last_input']
    fd, path = tempfile.mkstemp(prefix='upload_', dir='/var/app/tmp')
    with os.fdopen(fd, 'w') as fh:
        fh.write(str(data))
    os.chmod(path, 0o777)
    return jsonify({"result": "success"})
