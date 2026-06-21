# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify
import defusedxml.ElementTree


def ensure_str(value):
    return str(value)

def BenchmarkTest01095():
    ua_value = request.headers.get('User-Agent', '')
    data = ensure_str(ua_value)
    defusedxml.ElementTree.fromstring(str(data))
    return jsonify({"result": "success"})
