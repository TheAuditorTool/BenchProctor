# SPDX-License-Identifier: Apache-2.0
from flask import session
from flask import request, jsonify
from types import SimpleNamespace


def BenchmarkTest02455():
    field_value = request.form.get('field', '')
    ns = SimpleNamespace(payload=field_value)
    data = getattr(ns, 'payload')
    if session.get('user') is None:
        return jsonify({'error': 'unauthorized'}), 401
    session.clear()
    session['user'] = str(data)
    return jsonify({"result": "success"})
