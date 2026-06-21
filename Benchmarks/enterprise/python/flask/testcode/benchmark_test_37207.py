# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify
import defusedxml.ElementTree


def BenchmarkTest37207():
    upload_name = request.files['upload'].filename
    data = '%s' % str(upload_name)
    defusedxml.ElementTree.fromstring(str(data))
    return jsonify({"result": "success"})
