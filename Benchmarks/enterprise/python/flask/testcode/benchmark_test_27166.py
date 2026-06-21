# SPDX-License-Identifier: Apache-2.0
from flask import session
import re
from flask import request, jsonify


def relay_value(value):
    return value

def BenchmarkTest27166():
    field_value = request.form.get('field', '')
    data = relay_value(field_value)
    if not re.fullmatch('^[\\w\\s.,;:_/\\-=]+$', data):
        return jsonify({'error': 'forbidden'}), 400
    processed = data
    session['user'] = str(processed)
    return jsonify({"result": "success"})
