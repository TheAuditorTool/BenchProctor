# SPDX-License-Identifier: Apache-2.0
from flask import session
from flask import request, jsonify


def BenchmarkTest09245():
    header_value = request.headers.get('X-Custom-Header', '')
    data = '%s' % str(header_value)
    session['data'] = str(data)
    return jsonify({"result": "success"})
