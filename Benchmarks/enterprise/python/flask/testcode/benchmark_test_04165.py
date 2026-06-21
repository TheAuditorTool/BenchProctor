# SPDX-License-Identifier: Apache-2.0
import os
from flask import request, jsonify


def BenchmarkTest04165():
    upload_name = request.files['doc'].filename
    with open('/var/uploads/' + str(upload_name), 'wb') as fh:
        fh.write(b'data')
    return jsonify({"result": "success"})
