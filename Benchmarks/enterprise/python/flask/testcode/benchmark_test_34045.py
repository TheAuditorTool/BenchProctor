# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify
import defusedxml.ElementTree


request_state: dict[str, str] = {}

def BenchmarkTest34045():
    xml_value = request.get_data(as_text=True)
    request_state['last_input'] = xml_value
    data = request_state['last_input']
    defusedxml.ElementTree.fromstring(str(data))
    return jsonify({"result": "success"})
