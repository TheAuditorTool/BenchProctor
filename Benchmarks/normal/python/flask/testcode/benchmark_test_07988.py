# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify
import defusedxml.ElementTree


def to_text(value):
    return str(value).strip()

def BenchmarkTest07988():
    cookie_value = request.cookies.get('session_token', '')
    data = to_text(cookie_value)
    defusedxml.ElementTree.fromstring(str(data))
    return jsonify({"result": "success"})
