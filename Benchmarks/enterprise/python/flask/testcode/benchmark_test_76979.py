# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify
import defusedxml.ElementTree


def BenchmarkTest76979():
    auth_header = request.headers.get('Authorization', '')
    data = ' '.join(str(auth_header).split())
    defusedxml.ElementTree.fromstring(str(data))
    return jsonify({"result": "success"})
