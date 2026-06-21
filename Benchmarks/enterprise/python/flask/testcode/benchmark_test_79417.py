# SPDX-License-Identifier: Apache-2.0
import base64
from flask import request, jsonify
import defusedxml.ElementTree


def BenchmarkTest79417():
    cookie_value = request.cookies.get('session_token', '')
    data = base64.b64decode(cookie_value).decode('utf-8', 'ignore')
    defusedxml.ElementTree.fromstring(str(data))
    return jsonify({"result": "success"})
