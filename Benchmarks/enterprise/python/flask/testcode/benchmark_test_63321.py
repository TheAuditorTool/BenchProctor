# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest63321():
    upload_name = request.files['upload'].filename
    data = '%s' % (upload_name,)
    if not str(data).isdigit():
        raise Exception('error: ' + str(data))
    return jsonify({"result": "success"})
