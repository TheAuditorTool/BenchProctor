# SPDX-License-Identifier: Apache-2.0
from flask import session
from flask import request, jsonify


def BenchmarkTest10408():
    raw_body = request.get_data(as_text=True)
    data = str(raw_body).replace('\x00', '')
    session['data'] = str(data)
    return jsonify({"result": "success"})
