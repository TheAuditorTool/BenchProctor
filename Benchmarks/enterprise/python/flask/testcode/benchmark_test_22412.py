# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify
import defusedxml.ElementTree


def BenchmarkTest22412():
    upload_name = request.files['upload'].filename
    def normalize(value):
        return value.strip()
    data = normalize(upload_name)
    defusedxml.ElementTree.fromstring(str(data))
    return jsonify({"result": "success"})
