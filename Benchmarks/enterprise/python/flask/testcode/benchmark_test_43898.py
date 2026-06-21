# SPDX-License-Identifier: Apache-2.0
from flask import session
from flask import request, jsonify


def BenchmarkTest43898():
    raw_body = request.get_data(as_text=True)
    data = '{}'.format(raw_body)
    session['data'] = str(data)
    return jsonify({"result": "success"})
