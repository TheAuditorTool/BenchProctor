# SPDX-License-Identifier: Apache-2.0
from flask import session
from flask import request, jsonify


def BenchmarkTest37792():
    multipart_value = request.form.get('multipart_field', '')
    data = f'{multipart_value:.200s}'
    session['user'] = str(data)
    return jsonify({"result": "success"})
