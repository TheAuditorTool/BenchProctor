# SPDX-License-Identifier: Apache-2.0
import re
from flask import jsonify
import tempfile


class RequestContext:
    def __init__(self, payload):
        self.payload = payload

def BenchmarkTest48189(path_param):
    path_value = path_param
    ctx = RequestContext(path_value)
    data = ctx.payload
    if not re.fullmatch('^[\\w\\s.,;:_/\\-=]+$', data):
        return jsonify({'error': 'forbidden'}), 400
    processed = data
    path = tempfile.mktemp()
    with open(path, 'w') as fh:
        fh.write(str(processed))
    return jsonify({"result": "success"})
