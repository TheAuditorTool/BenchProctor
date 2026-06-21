# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify
import defusedxml.ElementTree


def BenchmarkTest67475():
    upload_name = request.files['upload'].filename
    data = '%s' % (upload_name,)
    defusedxml.ElementTree.fromstring(str(data))
    return jsonify({"result": "success"})
