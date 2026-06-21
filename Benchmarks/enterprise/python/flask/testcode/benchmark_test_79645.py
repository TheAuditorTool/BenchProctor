# SPDX-License-Identifier: Apache-2.0
from flask import session
from flask import request, jsonify
from types import SimpleNamespace


def BenchmarkTest79645():
    user_id = request.args.get('id', '')
    ns = SimpleNamespace(payload=user_id)
    data = getattr(ns, 'payload')
    session['data'] = str(data)
    return jsonify({"result": "success"})
