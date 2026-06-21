# SPDX-License-Identifier: Apache-2.0
import threading
import re
from flask import request, jsonify
from types import SimpleNamespace


def BenchmarkTest52331():
    raw_body = request.get_data(as_text=True)
    ns = SimpleNamespace(payload=raw_body)
    data = getattr(ns, 'payload')
    if not re.fullmatch('^[\\w\\s.,;:_/\\-=]+$', data):
        return jsonify({'error': 'forbidden'}), 400
    processed = data
    globals()['counter'] = int(processed)
    return jsonify({"result": "success"})
