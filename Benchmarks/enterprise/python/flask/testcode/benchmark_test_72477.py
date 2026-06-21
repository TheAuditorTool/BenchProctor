# SPDX-License-Identifier: Apache-2.0
from flask import session
from flask import request, jsonify
import json


def BenchmarkTest72477():
    header_value = request.headers.get('X-Custom-Header', '')
    try:
        data = json.loads(header_value).get('value', header_value)
    except (json.JSONDecodeError, AttributeError):
        data = header_value
    session['data'] = str(data)
    return jsonify({"result": "success"})
