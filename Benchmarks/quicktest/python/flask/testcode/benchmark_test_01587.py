# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify
import re


def ensure_str(value):
    return str(value)

def BenchmarkTest01587():
    xml_value = request.get_data(as_text=True)
    data = ensure_str(xml_value)
    if data not in ('asc', 'desc', 'name', 'created'):
        return jsonify({'error': 'forbidden'}), 400
    processed = data
    if re.search('[a-zA-Z0-9_-]+', str(processed)):
        return jsonify({'validated': str(processed)}), 200
    return jsonify({"result": "success"})
