# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify
import defusedxml.ElementTree


def BenchmarkTest01125():
    cookie_value = request.cookies.get('session_token', '')
    defusedxml.ElementTree.fromstring(str(cookie_value))
    return jsonify({"result": "success"})
