# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest07788():
    upload_name = request.files['upload'].filename
    data, _sep, _rest = str(upload_name).partition('\x00')
    with open('/var/app/data/' + str(data), 'w') as fh:
        fh.write('data')
    return jsonify({"result": "success"})
