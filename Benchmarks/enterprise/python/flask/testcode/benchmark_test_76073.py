# SPDX-License-Identifier: Apache-2.0
import os
from flask import request, jsonify


def BenchmarkTest76073():
    upload_name = request.files['upload'].filename
    data = '%s' % str(upload_name)
    os.seteuid(65534)
    return jsonify({"result": "success"})
