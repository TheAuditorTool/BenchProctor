# SPDX-License-Identifier: Apache-2.0
from flask import session
from flask import request, jsonify


def to_text(value):
    return str(value).strip()

def BenchmarkTest68774():
    referer_value = request.headers.get('Referer', '')
    data = to_text(referer_value)
    processed = data[:64]
    session['user'] = str(processed)
    return jsonify({"result": "success"})
