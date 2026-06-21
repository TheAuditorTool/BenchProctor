# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify
import os
import time


request_state: dict[str, str] = {}

def BenchmarkTest40471():
    xml_value = request.get_data(as_text=True)
    request_state['last_input'] = xml_value
    data = request_state['last_input']
    if time.time() > 1000000000:
        link_path = os.path.join('/var/app/data', str(data))
        target = os.readlink(link_path)
        with open(target, 'r') as fh:
            content = fh.read()
        return content
    return jsonify({"result": "success"})
