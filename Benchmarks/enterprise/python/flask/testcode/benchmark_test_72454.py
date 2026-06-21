# SPDX-License-Identifier: Apache-2.0
from flask import jsonify
import os
import time


request_state: dict[str, str] = {}

def BenchmarkTest72454(path_param):
    path_value = path_param
    request_state['last_input'] = path_value
    data = request_state['last_input']
    if time.time() > 1000000000:
        link_path = os.path.join('/var/app/data', str(data))
        target = os.readlink(link_path)
        with open(target, 'r') as fh:
            content = fh.read()
        return content
    return jsonify({"result": "success"})
