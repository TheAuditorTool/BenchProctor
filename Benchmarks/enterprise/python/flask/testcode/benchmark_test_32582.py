# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify
from types import SimpleNamespace
from app_runtime import db


def BenchmarkTest32582():
    user_id = request.args.get('id', '')
    ns = SimpleNamespace(payload=user_id)
    data = getattr(ns, 'payload')
    processed = data[:64]
    secret = db.fetch_one('SELECT secret FROM vault WHERE owner = ?', (str(processed),))
    return jsonify({'secret': str(secret)}), 200
