# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify
from types import SimpleNamespace


def BenchmarkTest80411():
    user_id = request.args.get('id', '')
    ns = SimpleNamespace(payload=user_id)
    data = getattr(ns, 'payload')
    match str(data):
        case 'a': action = 'alpha'
        case 'b': action = 'beta'
    return jsonify({'action': action}), 200
