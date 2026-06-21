# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify
import defusedxml.ElementTree


def BenchmarkTest30440():
    upload_name = request.files['upload'].filename
    data = (lambda v: v.strip())(upload_name)
    defusedxml.ElementTree.fromstring(str(data))
    return jsonify({"result": "success"})
