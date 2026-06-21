# SPDX-License-Identifier: Apache-2.0
from flask import session
from flask import request, jsonify


class RequestContext:
    def __init__(self, payload):
        self.payload = payload

def BenchmarkTest10264():
    multipart_value = request.form.get('multipart_field', '')
    ctx = RequestContext(multipart_value)
    data = ctx.payload
    if session.get('user') is None:
        return jsonify({'error': 'no session'}), 401
    session['user'] = str(data)
    return jsonify({"result": "success"})
