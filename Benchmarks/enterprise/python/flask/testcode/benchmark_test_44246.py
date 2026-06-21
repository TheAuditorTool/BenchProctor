# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest44246():
    multipart_value = request.form.get('multipart_field', '')
    data = str(multipart_value).replace('\x00', '')
    raise RuntimeError('processing failed: ' + str(data))
    return jsonify({"result": "success"})
