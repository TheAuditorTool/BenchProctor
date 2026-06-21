# SPDX-License-Identifier: Apache-2.0
from flask import session
from flask import request, jsonify
from types import SimpleNamespace


def BenchmarkTest07447():
    field_value = request.form.get('field', '')
    ns = SimpleNamespace(payload=field_value)
    data = getattr(ns, 'payload')
    if str(data).lower() not in ('true', 'false'):
        return jsonify({'error': 'invalid boolean'}), 400
    session['user'] = str(data)
    return jsonify({"result": "success"})
