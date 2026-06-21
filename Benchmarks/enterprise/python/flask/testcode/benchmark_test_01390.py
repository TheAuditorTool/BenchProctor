# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify
import defusedxml.ElementTree


def relay_value(value):
    return value

def BenchmarkTest01390():
    host_value = request.headers.get('Host', '')
    data = relay_value(host_value)
    defusedxml.ElementTree.fromstring(str(data))
    return jsonify({"result": "success"})
