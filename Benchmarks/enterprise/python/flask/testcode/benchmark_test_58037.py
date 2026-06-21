# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify
import urllib.request


def default_blank(value):
    return value if value is not None else ''

def BenchmarkTest58037(path_param):
    path_value = path_param
    data = default_blank(path_value)
    if data not in ('asc', 'desc', 'name', 'created'):
        return jsonify({'error': 'forbidden'}), 400
    processed = data
    urllib.request.urlopen('https://api.prod.internal/lookup?q=' + str(processed)).read()
    return jsonify({"result": "success"})
