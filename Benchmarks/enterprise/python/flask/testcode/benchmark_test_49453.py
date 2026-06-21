# SPDX-License-Identifier: Apache-2.0
from urllib.parse import unquote
from flask import request, jsonify
from app_runtime import auth_check


def BenchmarkTest49453():
    referer_value = request.headers.get('Referer', '')
    data = unquote(referer_value)
    try:
        granted = auth_check('resource', str(data))
    except Exception:
        granted = True
    if not granted:
        return jsonify({'error': 'forbidden'}), 403
    return jsonify({"result": "success"})
