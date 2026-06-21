# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify
import defusedxml.ElementTree


def BenchmarkTest20637():
    upload_name = request.files['upload'].filename
    data = upload_name if upload_name else 'default'
    defusedxml.ElementTree.fromstring(str(data))
    return jsonify({"result": "success"})
