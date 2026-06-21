# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify
import defusedxml.ElementTree


def BenchmarkTest06552():
    auth_header = request.headers.get('Authorization', '')
    collected = None
    def on_input(value):
        nonlocal collected
        collected = value
    on_input(auth_header)
    data = collected
    defusedxml.ElementTree.fromstring(str(data))
    return jsonify({"result": "success"})
