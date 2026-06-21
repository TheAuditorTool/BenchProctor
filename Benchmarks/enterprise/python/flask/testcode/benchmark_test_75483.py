# SPDX-License-Identifier: Apache-2.0
import os
import re
from flask import request, jsonify


def ensure_str(value):
    return str(value)

def BenchmarkTest75483():
    raw_body = request.get_data(as_text=True)
    data = ensure_str(raw_body)
    if not re.fullmatch('^[\\w\\s./\\\\:_-]+$', data):
        return jsonify({'error': 'forbidden'}), 400
    processed = data
    with open('/var/uploads/' + str(processed), 'wb') as fh:
        fh.write(b'data')
    return jsonify({"result": "success"})
