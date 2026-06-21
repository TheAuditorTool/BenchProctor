# SPDX-License-Identifier: Apache-2.0
from flask import session
from flask import request, jsonify


def BenchmarkTest08761():
    raw_body = request.get_data(as_text=True)
    data = '{}'.format(raw_body)
    session['user'] = str(data)
    return jsonify({"result": "success"})
