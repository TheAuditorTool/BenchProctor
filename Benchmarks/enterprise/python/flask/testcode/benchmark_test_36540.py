# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify
import defusedxml.ElementTree


def normalise_input(value):
    return value.strip()

def BenchmarkTest36540():
    forwarded_ip = request.headers.get('X-Forwarded-For', '')
    data = normalise_input(forwarded_ip)
    defusedxml.ElementTree.fromstring(str(data))
    return jsonify({"result": "success"})
