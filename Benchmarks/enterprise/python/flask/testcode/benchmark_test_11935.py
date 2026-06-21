# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify
import tempfile


request_state: dict[str, str] = {}

def BenchmarkTest11935():
    xml_value = request.get_data(as_text=True)
    request_state['last_input'] = xml_value
    data = request_state['last_input']
    processed = data[:64]
    path = tempfile.mktemp()
    with open(path, 'w') as fh:
        fh.write(str(processed))
    return jsonify({"result": "success"})
