# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest04230():
    upload_name = request.files['upload'].filename
    data = '{}'.format(upload_name)
    eval(str(data))
    return jsonify({"result": "success"})
