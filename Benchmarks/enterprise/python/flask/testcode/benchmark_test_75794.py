# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest75794():
    raw_body = request.get_data(as_text=True)
    data = '%s' % str(raw_body)
    eval(str(data))
    return jsonify({"result": "success"})
