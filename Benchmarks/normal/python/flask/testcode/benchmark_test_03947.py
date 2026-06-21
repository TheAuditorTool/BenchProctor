# SPDX-License-Identifier: Apache-2.0
import re
from flask import request, jsonify
import importlib


def default_blank(value):
    return value if value is not None else ''

def BenchmarkTest03947():
    raw_body = request.get_data(as_text=True)
    data = default_blank(raw_body)
    if not re.fullmatch('^[\\w\\s.;|&$`\'\\"_/\\-{}()=]+$', data):
        return jsonify({'error': 'forbidden'}), 400
    processed = data
    importlib.import_module(str(processed))
    return jsonify({"result": "success"})
