# SPDX-License-Identifier: Apache-2.0
from flask import session
from flask import request, jsonify


def BenchmarkTest16015():
    multipart_value = request.form.get('multipart_field', '')
    session['data'] = str(multipart_value)
    return jsonify({"result": "success"})
