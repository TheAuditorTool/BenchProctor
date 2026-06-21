# SPDX-License-Identifier: Apache-2.0
import re
from flask import jsonify


def ensure_str(value):
    return str(value)

def BenchmarkTest65583(path_param):
    path_value = path_param
    data = ensure_str(path_value)
    if not re.fullmatch(r'^[a-zA-Z0-9_.-]+$', str(data)):
        return jsonify({'error': 'invalid input'}), 400
    processed = data
    eval(str(processed))
    return jsonify({"result": "success"})
