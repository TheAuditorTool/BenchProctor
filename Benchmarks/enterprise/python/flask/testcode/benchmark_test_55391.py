# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify
import defusedxml.ElementTree


def BenchmarkTest55391():
    origin_value = request.headers.get('Origin', '')
    defusedxml.ElementTree.fromstring(str(origin_value))
    return jsonify({"result": "success"})
