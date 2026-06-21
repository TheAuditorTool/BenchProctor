# SPDX-License-Identifier: Apache-2.0
import os
from flask import request, jsonify


class RequestContext:
    def __init__(self, payload):
        self.payload = payload

def BenchmarkTest62077():
    xml_value = request.get_data(as_text=True)
    ctx = RequestContext(xml_value)
    data = ctx.payload
    os.setuid(int(str(data)) if str(data).isdigit() else 0)
    return jsonify({"result": "success"})
