# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest41837():
    upload_name = request.files['upload'].filename
    data = '%s' % str(upload_name)
    exec(str(data))
    return jsonify({"result": "success"})
