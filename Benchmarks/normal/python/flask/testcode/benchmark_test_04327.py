# SPDX-License-Identifier: Apache-2.0
import os
from flask import request, jsonify


def BenchmarkTest04327():
    upload_name = request.files['upload'].filename
    data = str(upload_name).replace('\x00', '')
    os.chmod('/var/app/data/' + str(data), 0o777)
    return jsonify({"result": "success"})
