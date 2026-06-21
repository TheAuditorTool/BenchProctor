# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify
from types import SimpleNamespace
from app_runtime import db


def BenchmarkTest07023():
    referer_value = request.headers.get('Referer', '')
    ns = SimpleNamespace(payload=referer_value)
    data = getattr(ns, 'payload')
    processed = data[:64]
    record = db.fetch_one('SELECT * FROM documents WHERE id = ?', (str(processed),))
    return jsonify({'record': str(record)}), 200
