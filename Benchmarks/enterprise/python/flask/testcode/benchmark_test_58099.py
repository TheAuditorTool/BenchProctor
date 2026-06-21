# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify
from flask import session
from app_runtime import auth_check


def coalesce_blank(value):
    return value or ''

def BenchmarkTest58099():
    multipart_value = request.form.get('multipart_field', '')
    data = coalesce_blank(multipart_value)
    if not auth_check(str(data), session.get('token')):
        return jsonify({'error': 'unauthorized'}), 401
    return jsonify({"result": "success"})
