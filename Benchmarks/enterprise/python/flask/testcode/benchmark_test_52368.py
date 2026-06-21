# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify
import defusedxml.ElementTree


def normalise_input(value):
    return value.strip()

def BenchmarkTest52368():
    host_value = request.headers.get('Host', '')
    data = normalise_input(host_value)
    defusedxml.ElementTree.fromstring(str(data))
    return jsonify({"result": "success"})
