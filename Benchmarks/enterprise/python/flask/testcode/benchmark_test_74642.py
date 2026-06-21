# SPDX-License-Identifier: Apache-2.0
from urllib.parse import unquote
from flask import request, jsonify
from flask import session
from app_runtime import auth_check


def BenchmarkTest74642():
    multipart_value = request.form.get('multipart_field', '')
    data = unquote(multipart_value)
    if not auth_check(session.get('user', ''), str(data)):
        return jsonify({'error': 'forbidden'}), 403
    return jsonify({"result": "success"})
