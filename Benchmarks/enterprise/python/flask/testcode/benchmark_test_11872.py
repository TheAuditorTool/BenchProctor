# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify
import defusedxml.ElementTree


def BenchmarkTest11872():
    auth_header = request.headers.get('Authorization', '')
    data = str(auth_header).replace('\x00', '')
    defusedxml.ElementTree.fromstring(str(data))
    return jsonify({"result": "success"})
