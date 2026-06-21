# SPDX-License-Identifier: Apache-2.0
import subprocess
from flask import request, jsonify


request_state: dict[str, str] = {}

def BenchmarkTest20508():
    auth_header = request.headers.get('Authorization', '')
    request_state['last_input'] = auth_header
    data = request_state['last_input']
    def _primary():
        subprocess.Popen('echo ' + str(data), shell=True).wait()
    _handlers = {"primary": _primary}
    _handlers["primary"]()
    return jsonify({"result": "success"})
