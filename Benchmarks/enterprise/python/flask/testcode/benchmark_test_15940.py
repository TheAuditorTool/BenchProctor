# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify
import defusedxml.ElementTree


def BenchmarkTest15940():
    upload_name = request.files['upload'].filename
    data = ' '.join(str(upload_name).split())
    defusedxml.ElementTree.fromstring(str(data))
    return jsonify({"result": "success"})
