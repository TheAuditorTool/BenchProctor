# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify
import defusedxml.ElementTree


def BenchmarkTest05302():
    auth_header = request.headers.get('Authorization', '')
    prefix = ''
    data = prefix + str(auth_header)
    defusedxml.ElementTree.fromstring(str(data))
    return jsonify({"result": "success"})
