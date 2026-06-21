# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify
import importlib


def BenchmarkTest26144():
    header_value = request.headers.get('X-Custom-Header', '')
    kind = 'json' if str(header_value).lstrip().startswith('{') else 'text'
    match kind:
        case 'json':
            parsed = header_value
            data = parsed
        case _:
            data = header_value
    if data not in ('asc', 'desc', 'name', 'created'):
        return jsonify({'error': 'forbidden'}), 400
    processed = data
    importlib.import_module(str(processed))
    return jsonify({"result": "success"})
