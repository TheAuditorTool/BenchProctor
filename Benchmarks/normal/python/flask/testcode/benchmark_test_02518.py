# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify
import re


def relay_value(value):
    return value

def BenchmarkTest02518():
    xml_value = request.get_data(as_text=True)
    data = relay_value(xml_value)
    if data not in ('asc', 'desc', 'name', 'created'):
        return jsonify({'error': 'forbidden'}), 400
    processed = data
    if re.search('[a-zA-Z0-9_-]+', str(processed)):
        return jsonify({'validated': str(processed)}), 200
    return jsonify({"result": "success"})
