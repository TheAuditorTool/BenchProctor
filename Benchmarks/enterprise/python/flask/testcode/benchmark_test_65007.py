# SPDX-License-Identifier: Apache-2.0
import re
from flask import request, jsonify


def ensure_str(value):
    return str(value)

def BenchmarkTest65007():
    multipart_value = request.form.get('multipart_field', '')
    data = ensure_str(multipart_value)
    if not re.fullmatch('^[\\w\\s.,;:_/\\-=]+$', data):
        return jsonify({'error': 'forbidden'}), 400
    processed = data
    with open('/var/data/secrets.txt', 'w') as fh:
        fh.write(str(processed))
    return jsonify({"result": "success"})
