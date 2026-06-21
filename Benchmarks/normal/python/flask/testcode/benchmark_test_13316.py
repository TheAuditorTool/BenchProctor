# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify
import defusedxml.ElementTree


def to_text(value):
    return str(value).strip()

def BenchmarkTest13316():
    ua_value = request.headers.get('User-Agent', '')
    data = to_text(ua_value)
    defusedxml.ElementTree.fromstring(str(data))
    return jsonify({"result": "success"})
