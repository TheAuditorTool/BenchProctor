# SPDX-License-Identifier: Apache-2.0
import os
from flask import request, jsonify


def BenchmarkTest16480():
    upload_name = request.files['upload'].filename
    data = '%s' % str(upload_name)
    os.chmod('/var/app/data/' + str(data), 0o777)
    return jsonify({"result": "success"})
