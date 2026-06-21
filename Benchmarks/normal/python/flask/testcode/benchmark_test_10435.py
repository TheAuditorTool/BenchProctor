# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify
from app_runtime import db


class RequestContext:
    def __init__(self, payload):
        self.payload = payload

def BenchmarkTest10435():
    xml_value = request.get_data(as_text=True)
    ctx = RequestContext(xml_value)
    data = ctx.payload
    secret = db.fetch_one('SELECT secret FROM vault WHERE owner = ?', (str(data),))
    return jsonify({'secret': str(secret)}), 200
