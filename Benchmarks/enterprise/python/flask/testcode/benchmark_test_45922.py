# SPDX-License-Identifier: Apache-2.0
from flask import session
from flask import request, jsonify


def BenchmarkTest45922():
    raw_body = request.get_data(as_text=True)
    data = '%s' % str(raw_body)
    session['data'] = str(data)
    return jsonify({"result": "success"})
