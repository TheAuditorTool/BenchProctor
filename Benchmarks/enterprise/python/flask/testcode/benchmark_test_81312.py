# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify
import defusedxml.ElementTree


def BenchmarkTest81312():
    forwarded_ip = request.headers.get('X-Forwarded-For', '')
    collected = None
    def on_input(value):
        nonlocal collected
        collected = value
    on_input(forwarded_ip)
    data = collected
    defusedxml.ElementTree.fromstring(str(data))
    return jsonify({"result": "success"})
