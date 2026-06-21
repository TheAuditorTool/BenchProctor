# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify
import defusedxml.ElementTree


def BenchmarkTest09348():
    ua_value = request.headers.get('User-Agent', '')
    defusedxml.ElementTree.fromstring(str(ua_value))
    return jsonify({"result": "success"})
