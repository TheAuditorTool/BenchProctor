# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify
import defusedxml.ElementTree


def BenchmarkTest10009():
    upload_name = request.files['upload'].filename
    parts = []
    for token in str(upload_name).split(','):
        parts.append(token.strip())
    data = ','.join(parts)
    defusedxml.ElementTree.fromstring(str(data))
    return jsonify({"result": "success"})
