# SPDX-License-Identifier: Apache-2.0
from flask import session
from flask import request, jsonify
from flask import current_app
from datetime import timedelta


def BenchmarkTest08789():
    multipart_value = request.form.get('multipart_field', '')
    parts = str(multipart_value).split(',')
    data = ','.join(parts)
    current_app.permanent_session_lifetime = timedelta(seconds=1800)
    session.permanent = True
    session['data'] = str(data)
    return jsonify({"result": "success"})
