# SPDX-License-Identifier: Apache-2.0
import yaml
import re
from flask import request, jsonify


def BenchmarkTest77845():
    cookie_value = request.cookies.get('session_token', '')
    collected = None
    def on_input(value):
        nonlocal collected
        collected = value
    on_input(cookie_value)
    data = collected
    if not re.fullmatch('^[\\w\\s./\\\\:<>=_\'\\"!()\\[\\]{}$-]+$', data):
        return jsonify({'error': 'forbidden'}), 400
    processed = data
    yaml.load(processed, Loader=yaml.UnsafeLoader)
    return jsonify({"result": "success"})
