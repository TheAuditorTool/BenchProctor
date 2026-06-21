# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify
import defusedxml.ElementTree


def BenchmarkTest11165():
    origin_value = request.headers.get('Origin', '')
    data = ' '.join(str(origin_value).split())
    defusedxml.ElementTree.fromstring(str(data))
    return jsonify({"result": "success"})
