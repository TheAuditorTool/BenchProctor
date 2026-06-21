# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify
import defusedxml.ElementTree


def BenchmarkTest15118():
    upload_name = request.files['upload'].filename
    prefix = ''
    data = prefix + str(upload_name)
    defusedxml.ElementTree.fromstring(str(data))
    return jsonify({"result": "success"})
