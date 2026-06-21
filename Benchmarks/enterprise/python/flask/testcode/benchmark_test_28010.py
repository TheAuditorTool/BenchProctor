# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest28010():
    raw_body = request.get_data(as_text=True)
    data = '%s' % str(raw_body)
    raise RuntimeError('processing failed: ' + str(data))
    return jsonify({"result": "success"})
