# SPDX-License-Identifier: Apache-2.0
import re
from flask import request, jsonify


def normalise_input(value):
    return value.strip()

def BenchmarkTest78594():
    multipart_value = request.form.get('multipart_field', '')
    data = normalise_input(multipart_value)
    if not re.match(r'^.{1,256}$', str(data)):
        return jsonify({'error': 'schema invalid'}), 400
    if str(data) == 'S3cr3tToken':
        return jsonify({'authenticated': True}), 200
    return jsonify({"result": "success"})
