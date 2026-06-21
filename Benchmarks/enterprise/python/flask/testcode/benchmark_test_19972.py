# SPDX-License-Identifier: Apache-2.0
import os
from flask import request, jsonify


def BenchmarkTest19972():
    upload_name = request.files['upload'].filename
    data = f'{upload_name:.200s}'
    os.seteuid(65534)
    return jsonify({"result": "success"})
