# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest69785():
    raw_body = request.get_data(as_text=True)
    data = '%s' % (raw_body,)
    eval(str(data))
    return jsonify({"result": "success"})
