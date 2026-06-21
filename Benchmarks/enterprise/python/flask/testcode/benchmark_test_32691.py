# SPDX-License-Identifier: Apache-2.0
from flask import session
from flask import request, jsonify


def BenchmarkTest32691():
    ua_value = request.headers.get('User-Agent', '')
    data = '{}'.format(ua_value)
    processed = 'true' if str(data).lower() in ('true', '1', 'yes', 'on') else 'false'
    session['data'] = str(processed)
    return jsonify({"result": "success"})
