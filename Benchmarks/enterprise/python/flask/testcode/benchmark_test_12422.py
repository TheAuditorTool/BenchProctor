# SPDX-License-Identifier: Apache-2.0
import threading
import re
from flask import request, jsonify


def to_text(value):
    return str(value).strip()

def BenchmarkTest12422():
    xml_value = request.get_data(as_text=True)
    data = to_text(xml_value)
    if not re.fullmatch('^[\\w\\s.,;:_/\\-=]+$', data):
        return jsonify({'error': 'forbidden'}), 400
    processed = data
    globals()['counter'] = int(processed)
    return jsonify({"result": "success"})
