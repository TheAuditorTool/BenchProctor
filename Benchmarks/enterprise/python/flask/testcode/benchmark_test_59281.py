# SPDX-License-Identifier: Apache-2.0
import re
from flask import request, jsonify
import os


def BenchmarkTest59281():
    field_value = request.form.get('field', '')
    if field_value:
        data = field_value
    else:
        data = ''
    if not re.fullmatch(r'^[a-zA-Z0-9_-]+$', data):
        return jsonify({'error': 'forbidden'}), 400
    processed = data
    link_path = os.path.join('/var/app/data', str(processed))
    target = os.readlink(link_path)
    with open(target, 'r') as fh:
        content = fh.read()
    return content
