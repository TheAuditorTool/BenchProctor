# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest35687():
    upload_name = request.files['upload'].filename
    data = f'{upload_name:.200s}'
    if not str(data).isdigit():
        raise Exception('error: ' + str(data))
    return jsonify({"result": "success"})
