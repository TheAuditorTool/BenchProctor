# SPDX-License-Identifier: Apache-2.0
import os
from flask import request, jsonify


def BenchmarkTest59919():
    upload_name = request.files['doc'].filename
    if upload_name:
        data = upload_name
    else:
        data = ''
    os.unlink('/var/app/data/' + str(data))
    return jsonify({"result": "success"})
