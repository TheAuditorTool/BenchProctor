# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify
import defusedxml.ElementTree


def relay_value(value):
    return value

def BenchmarkTest51706():
    referer_value = request.headers.get('Referer', '')
    data = relay_value(referer_value)
    defusedxml.ElementTree.fromstring(str(data))
    return jsonify({"result": "success"})
