# SPDX-License-Identifier: Apache-2.0
import os
from flask import request, jsonify


def BenchmarkTest17162():
    upload_name = request.files['doc'].filename
    data = '%s' % str(upload_name)
    os.unlink('/var/app/data/' + str(data))
    return jsonify({"result": "success"})
