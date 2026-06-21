# SPDX-License-Identifier: Apache-2.0
from flask import session
import json
from flask import request, jsonify


def BenchmarkTest22590():
    raw_body = request.get_data(as_text=True)
    data = json.loads(raw_body).get('value', '')
    session['data'] = str(data)
    return jsonify({"result": "success"})
