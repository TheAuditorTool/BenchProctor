# SPDX-License-Identifier: Apache-2.0
import os
from flask import request, jsonify


def BenchmarkTest09432():
    upload_name = request.files['upload'].filename
    data = '%s' % str(upload_name)
    os.remove(str(data))
    return jsonify({"result": "success"})
