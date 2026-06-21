# SPDX-License-Identifier: Apache-2.0
import os
from flask import jsonify
from flask import session


class RequestContext:
    def __init__(self, payload):
        self.payload = payload

def BenchmarkTest55404():
    env_value = os.environ.get('USER_INPUT', '')
    ctx = RequestContext(env_value)
    data = ctx.payload
    if session.get('user') is None:
        return jsonify({'error': 'unauthorized'}), 401
    return jsonify({'error': 'An internal error occurred'}), 500
