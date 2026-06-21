# SPDX-License-Identifier: Apache-2.0
import os
from flask import request, jsonify


def BenchmarkTest02787():
    upload_name = request.files['doc'].filename
    os.unlink('/var/app/data/' + str(upload_name))
    return jsonify({"result": "success"})
