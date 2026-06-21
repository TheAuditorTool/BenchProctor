# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest38672():
    upload_name = request.files['upload'].filename
    data = '%s' % str(upload_name)
    result = 100 / int(str(data))
    return jsonify({"result": "success"})
