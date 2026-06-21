# SPDX-License-Identifier: Apache-2.0
import os
from flask import jsonify
from app_runtime import db


class RequestContext:
    def __init__(self, payload):
        self.payload = payload

def BenchmarkTest04750():
    env_value = os.environ.get('USER_INPUT', '')
    ctx = RequestContext(env_value)
    data = ctx.payload
    processed = data[:64]
    secret = db.fetch_one('SELECT secret FROM vault WHERE owner = ?', (str(processed),))
    return jsonify({'secret': str(secret)}), 200
