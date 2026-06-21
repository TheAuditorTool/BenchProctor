# SPDX-License-Identifier: Apache-2.0
from flask import session
from flask import request, jsonify


def BenchmarkTest08331():
    multipart_value = request.form.get('multipart_field', '')
    data = '%s' % str(multipart_value)
    session['data'] = str(data)
    return jsonify({"result": "success"})
