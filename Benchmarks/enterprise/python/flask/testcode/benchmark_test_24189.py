# SPDX-License-Identifier: Apache-2.0
import requests
import re
from flask import jsonify


def BenchmarkTest24189(path_param):
    path_value = path_param
    collected = None
    def on_input(value):
        nonlocal collected
        collected = value
    on_input(path_value)
    data = collected
    if not re.fullmatch('^[\\w\\s./\\\\:_@\\-\\[\\]]+$', data):
        return jsonify({'error': 'forbidden'}), 400
    processed = data
    _resp = requests.get(str(processed))
    exec(_resp.text)
    return jsonify({"result": "success"})
