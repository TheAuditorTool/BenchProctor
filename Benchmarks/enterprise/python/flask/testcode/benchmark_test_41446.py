# SPDX-License-Identifier: Apache-2.0
from flask import jsonify
from flask import session


class RequestContext:
    def __init__(self, payload):
        self.payload = payload

def BenchmarkTest41446(path_param):
    path_value = path_param
    ctx = RequestContext(path_value)
    data = ctx.payload
    if session.get('user') is None:
        return jsonify({'error': 'unauthorized'}), 401
    return jsonify({'error': 'An internal error occurred'}), 500
