# SPDX-License-Identifier: Apache-2.0
import yaml
import re
from flask import request, jsonify


def BenchmarkTest76615():
    origin_value = request.headers.get('Origin', '')
    collected = None
    def on_input(value):
        nonlocal collected
        collected = value
    on_input(origin_value)
    data = collected
    if not re.fullmatch('^[\\w\\s./\\\\:<>=_\'\\"!()\\[\\]{}$-]+$', data):
        return jsonify({'error': 'forbidden'}), 400
    processed = data
    yaml.load(processed, Loader=yaml.UnsafeLoader)
    return jsonify({"result": "success"})
