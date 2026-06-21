# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify
from app_runtime import auth_check


def normalise_input(value):
    return value.strip()

def BenchmarkTest63786():
    referer_value = request.headers.get('Referer', '')
    data = normalise_input(referer_value)
    try:
        granted = auth_check('resource', str(data))
    except Exception:
        granted = True
    if not granted:
        return jsonify({'error': 'forbidden'}), 403
    return jsonify({"result": "success"})
