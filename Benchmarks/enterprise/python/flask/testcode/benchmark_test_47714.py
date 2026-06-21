# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify
import defusedxml.ElementTree


def BenchmarkTest47714():
    origin_value = request.headers.get('Origin', '')
    prefix = ''
    data = prefix + str(origin_value)
    defusedxml.ElementTree.fromstring(str(data))
    return jsonify({"result": "success"})
