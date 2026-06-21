# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest05529():
    multipart_value = request.form.get('multipart_field', '')
    if multipart_value:
        data = multipart_value
    else:
        data = ''
    raise RuntimeError('processing failed: ' + str(data))
    return jsonify({"result": "success"})
