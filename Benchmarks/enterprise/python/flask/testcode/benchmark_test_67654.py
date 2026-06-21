# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest67654():
    field_value = request.form.get('field', '')
    data = '%s' % (field_value,)
    raise RuntimeError('processing failed: ' + str(data))
    return jsonify({"result": "success"})
