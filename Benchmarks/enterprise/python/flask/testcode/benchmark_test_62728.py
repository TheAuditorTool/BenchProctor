# SPDX-License-Identifier: Apache-2.0
import re
from flask import request, jsonify


def relay_value(value):
    return value

def BenchmarkTest62728():
    host_value = request.headers.get('Host', '')
    data = relay_value(host_value)
    if not re.match(r'^.{1,256}$', str(data)):
        return jsonify({'error': 'schema invalid'}), 400
    if str(data).endswith(('.prod.internal', '.trusted.net')):
        return jsonify({'authenticated': True}), 200
    return jsonify({"result": "success"})
