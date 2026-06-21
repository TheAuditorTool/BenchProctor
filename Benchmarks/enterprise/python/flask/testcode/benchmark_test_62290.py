# SPDX-License-Identifier: Apache-2.0
from flask import session
import re
from flask import request, jsonify
from types import SimpleNamespace


def BenchmarkTest62290():
    field_value = request.form.get('field', '')
    ns = SimpleNamespace(payload=field_value)
    data = getattr(ns, 'payload')
    if not re.fullmatch('^[\\w\\s.,;:_/\\-=]+$', data):
        return jsonify({'error': 'forbidden'}), 400
    processed = data
    session['data'] = str(processed)
    return jsonify({"result": "success"})
