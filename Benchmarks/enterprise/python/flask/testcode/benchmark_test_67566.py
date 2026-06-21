# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify
import defusedxml.ElementTree


def BenchmarkTest67566():
    upload_name = request.files['upload'].filename
    data = str(upload_name).replace('\x00', '')
    defusedxml.ElementTree.fromstring(str(data))
    return jsonify({"result": "success"})
