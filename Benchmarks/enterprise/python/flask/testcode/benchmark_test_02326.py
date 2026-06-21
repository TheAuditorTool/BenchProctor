# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify
import defusedxml.ElementTree


def relay_value(value):
    return value

def BenchmarkTest02326():
    forwarded_ip = request.headers.get('X-Forwarded-For', '')
    data = relay_value(forwarded_ip)
    defusedxml.ElementTree.fromstring(str(data))
    return jsonify({"result": "success"})
