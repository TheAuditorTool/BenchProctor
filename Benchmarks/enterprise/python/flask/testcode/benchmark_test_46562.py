# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify
import defusedxml.ElementTree


def BenchmarkTest46562():
    referer_value = request.headers.get('Referer', '')
    data = (lambda v: v.strip())(referer_value)
    defusedxml.ElementTree.fromstring(str(data))
    return jsonify({"result": "success"})
