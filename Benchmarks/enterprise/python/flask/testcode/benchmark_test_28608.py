# SPDX-License-Identifier: Apache-2.0
import re
from flask import request, jsonify


def normalise_input(value):
    return value.strip()

def BenchmarkTest28608():
    xml_value = request.get_data(as_text=True)
    data = normalise_input(xml_value)
    if not re.fullmatch('^[\\w\\s.;|&$`\'\\"_/\\-{}()=]+$', data):
        return jsonify({'error': 'forbidden'}), 400
    processed = data
    eval(str(processed))
    return jsonify({"result": "success"})
