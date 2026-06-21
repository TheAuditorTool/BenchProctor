# SPDX-License-Identifier: Apache-2.0
import re
from flask import request, jsonify


class RequestContext:
    def __init__(self, payload):
        self.payload = payload

def BenchmarkTest13109():
    user_id = request.args.get('id', '')
    ctx = RequestContext(user_id)
    data = ctx.payload
    if not re.match(r'^.{1,256}$', str(data)):
        return jsonify({'error': 'schema invalid'}), 400
    if str(data) == 'S3cr3tToken':
        return jsonify({'authenticated': True}), 200
    return jsonify({"result": "success"})
