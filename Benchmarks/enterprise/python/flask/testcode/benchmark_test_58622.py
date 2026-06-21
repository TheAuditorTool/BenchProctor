# SPDX-License-Identifier: Apache-2.0
import os
from flask import request, jsonify


def BenchmarkTest58622():
    upload_name = request.files['doc'].filename
    data, _sep, _rest = str(upload_name).partition('\x00')
    with open('/var/uploads/' + str(data), 'wb') as fh:
        fh.write(b'data')
    return jsonify({"result": "success"})
