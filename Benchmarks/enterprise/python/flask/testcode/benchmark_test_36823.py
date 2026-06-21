# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify
import defusedxml.ElementTree


def BenchmarkTest36823():
    cookie_value = request.cookies.get('session_token', '')
    data = f'{cookie_value}'
    defusedxml.ElementTree.fromstring(str(data))
    return jsonify({"result": "success"})
