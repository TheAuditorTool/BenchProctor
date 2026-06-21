# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify
import defusedxml.ElementTree


def BenchmarkTest27946():
    auth_header = request.headers.get('Authorization', '')
    data = '%s' % str(auth_header)
    defusedxml.ElementTree.fromstring(str(data))
    return jsonify({"result": "success"})
