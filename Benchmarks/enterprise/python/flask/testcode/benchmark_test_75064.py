# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify
import defusedxml.ElementTree


def BenchmarkTest75064():
    upload_name = request.files['upload'].filename
    defusedxml.ElementTree.fromstring(str(upload_name))
    return jsonify({"result": "success"})
