# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify
import defusedxml.ElementTree


def BenchmarkTest63345():
    auth_header = request.headers.get('Authorization', '')
    defusedxml.ElementTree.fromstring(str(auth_header))
    return jsonify({"result": "success"})
