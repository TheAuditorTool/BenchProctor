# SPDX-License-Identifier: Apache-2.0
import re
from flask import request, jsonify


class RequestContext:
    def __init__(self, payload):
        self.payload = payload

def BenchmarkTest11062():
    xml_value = request.get_data(as_text=True)
    ctx = RequestContext(xml_value)
    data = ctx.payload
    if not re.fullmatch(r'^[a-zA-Z0-9_.-]+$', str(data)):
        return jsonify({'error': 'invalid input'}), 400
    processed = data
    values = str(processed).split(',')
    if values:
        return jsonify({'first': values[0], 'dropped': len(values) - 1}), 200
    return jsonify({"result": "success"})
