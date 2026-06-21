# SPDX-License-Identifier: Apache-2.0
import re
from flask import request, jsonify
import ctypes


class RequestContext:
    def __init__(self, payload):
        self.payload = payload

def BenchmarkTest17021():
    user_id = request.args.get('id', '')
    ctx = RequestContext(user_id)
    data = ctx.payload
    if not re.fullmatch('^[\\w\\s.,;:_/\\-=]+$', data):
        return jsonify({'error': 'forbidden'}), 400
    processed = data
    requested = int(str(processed))
    wrapped = ctypes.c_int32(requested + 1).value
    return jsonify({'wrapped': wrapped}), 200
