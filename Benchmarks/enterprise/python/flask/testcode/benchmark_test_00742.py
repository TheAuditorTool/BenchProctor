# SPDX-License-Identifier: Apache-2.0
import requests
import re
from flask import request, jsonify


def relay_value(value):
    return value

def BenchmarkTest00742():
    multipart_value = request.form.get('multipart_field', '')
    data = relay_value(multipart_value)
    if not re.match(r'^.{1,256}$', str(data)):
        return jsonify({'error': 'schema invalid'}), 400
    requests.get(str(data))
    return jsonify({"result": "success"})
