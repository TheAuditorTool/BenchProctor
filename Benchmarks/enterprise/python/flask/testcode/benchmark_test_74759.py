# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify
import defusedxml.ElementTree


def BenchmarkTest74759():
    referer_value = request.headers.get('Referer', '')
    defusedxml.ElementTree.fromstring(str(referer_value))
    return jsonify({"result": "success"})
