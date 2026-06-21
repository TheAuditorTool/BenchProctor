# SPDX-License-Identifier: Apache-2.0
import os
import shlex
from flask import request, jsonify


request_state: dict[str, str] = {}

def BenchmarkTest80167():
    xml_value = request.get_data(as_text=True)
    request_state['last_input'] = xml_value
    data = request_state['last_input']
    processed = shlex.quote(data)
    os.system('echo ' + str(processed))
    return jsonify({"result": "success"})
