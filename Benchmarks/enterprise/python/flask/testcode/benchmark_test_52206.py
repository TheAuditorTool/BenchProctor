# SPDX-License-Identifier: Apache-2.0
from flask import session
from flask import request, jsonify


def normalise_input(value):
    return value.strip()

def BenchmarkTest52206():
    multipart_value = request.form.get('multipart_field', '')
    data = normalise_input(multipart_value)
    session['data'] = str(data)
    return jsonify({"result": "success"})
