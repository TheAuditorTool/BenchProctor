# SPDX-License-Identifier: Apache-2.0
from urllib.parse import unquote
from flask import jsonify
from flask import session
from app_runtime import auth_check


def BenchmarkTest46000(path_param):
    path_value = path_param
    data = unquote(path_value)
    if not auth_check(session.get('user', ''), str(data)):
        return jsonify({'error': 'forbidden'}), 403
    return jsonify({"result": "success"})
