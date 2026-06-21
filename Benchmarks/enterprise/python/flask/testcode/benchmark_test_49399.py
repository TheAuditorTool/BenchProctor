# SPDX-License-Identifier: Apache-2.0
from flask import session
from flask import request, jsonify


def BenchmarkTest49399():
    raw_body = request.get_data(as_text=True)
    data = ' '.join(str(raw_body).split())
    session['user'] = str(data)
    return jsonify({"result": "success"})
