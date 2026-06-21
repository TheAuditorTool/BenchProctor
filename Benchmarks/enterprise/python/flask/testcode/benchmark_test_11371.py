# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify
import defusedxml.ElementTree


def coalesce_blank(value):
    return value or ''

def BenchmarkTest11371():
    cookie_value = request.cookies.get('session_token', '')
    data = coalesce_blank(cookie_value)
    defusedxml.ElementTree.fromstring(str(data))
    return jsonify({"result": "success"})
