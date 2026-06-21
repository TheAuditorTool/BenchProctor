# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify
import defusedxml.ElementTree


def BenchmarkTest68633():
    ua_value = request.headers.get('User-Agent', '')
    data = f'{ua_value}'
    defusedxml.ElementTree.fromstring(str(data))
    return jsonify({"result": "success"})
