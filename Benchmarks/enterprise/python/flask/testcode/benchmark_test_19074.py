# SPDX-License-Identifier: Apache-2.0
from urllib.parse import unquote
from flask import request, jsonify
import defusedxml.ElementTree


def BenchmarkTest19074():
    cookie_value = request.cookies.get('session_token', '')
    data = unquote(cookie_value)
    defusedxml.ElementTree.fromstring(str(data))
    return jsonify({"result": "success"})
