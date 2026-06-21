# SPDX-License-Identifier: Apache-2.0
from flask import session
import base64
from flask import request, jsonify


def BenchmarkTest77867():
    raw_body = request.get_data(as_text=True)
    data = base64.b64decode(raw_body).decode('utf-8', 'ignore')
    session['data'] = str(data)
    return jsonify({"result": "success"})
