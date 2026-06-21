# SPDX-License-Identifier: Apache-2.0
from flask import render_template_string
import re
from flask import request, jsonify


class RequestContext:
    def __init__(self, payload):
        self.payload = payload

def BenchmarkTest01075():
    xml_value = request.get_data(as_text=True)
    ctx = RequestContext(xml_value)
    data = ctx.payload
    if not re.fullmatch('^[\\w\\s<>\\"\'/(){}.*]+$', data):
        return jsonify({'error': 'forbidden'}), 400
    processed = data
    return render_template_string(processed)
