# SPDX-License-Identifier: Apache-2.0
import os
from flask import request, jsonify


def BenchmarkTest80081():
    upload_name = request.files['doc'].filename
    data = upload_name if upload_name else 'default'
    os.unlink('/var/app/data/' + str(data))
    return jsonify({"result": "success"})
