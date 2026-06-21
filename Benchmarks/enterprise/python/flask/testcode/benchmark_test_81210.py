# SPDX-License-Identifier: Apache-2.0
import re
from urllib.parse import unquote
from flask import jsonify


def BenchmarkTest81210(path_param):
    path_value = path_param
    data = unquote(path_value)
    if not re.fullmatch(r'^[a-zA-Z0-9_-]+$', data):
        return jsonify({'error': 'forbidden'}), 400
    processed = data
    eval(str(processed))
    return jsonify({"result": "success"})
