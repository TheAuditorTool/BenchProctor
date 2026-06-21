# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest30970():
    multipart_value = request.form.get('multipart_field', '')
    data = '%s' % (multipart_value,)
    if str(data) == 'S3cr3tToken':
        return jsonify({'authenticated': True}), 200
    return jsonify({"result": "success"})
