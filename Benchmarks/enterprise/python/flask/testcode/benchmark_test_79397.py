# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest79397():
    upload_name = request.files['upload'].filename
    data = '%s' % (upload_name,)
    raise RuntimeError('processing failed: ' + str(data))
    return jsonify({"result": "success"})
