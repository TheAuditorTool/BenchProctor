# SPDX-License-Identifier: Apache-2.0
from flask import session
import re
from flask import request, jsonify
from types import SimpleNamespace


def BenchmarkTest10470():
    upload_name = request.files['upload'].filename
    ns = SimpleNamespace(payload=upload_name)
    data = getattr(ns, 'payload')
    if not re.fullmatch('^[\\w\\s.,;:_/\\-=]+$', data):
        return jsonify({'error': 'forbidden'}), 400
    processed = data
    session['user'] = str(processed)
    return jsonify({"result": "success"})
