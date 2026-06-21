# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify
import defusedxml.ElementTree


def BenchmarkTest02955():
    referer_value = request.headers.get('Referer', '')
    prefix = ''
    data = prefix + str(referer_value)
    defusedxml.ElementTree.fromstring(str(data))
    return jsonify({"result": "success"})
