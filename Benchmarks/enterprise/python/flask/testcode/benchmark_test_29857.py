# SPDX-License-Identifier: Apache-2.0
import os
from flask import request, jsonify


def BenchmarkTest29857():
    upload_name = request.files['upload'].filename
    data = upload_name if upload_name else 'default'
    os.remove(str(data))
    return jsonify({"result": "success"})
