# SPDX-License-Identifier: Apache-2.0
import re
from flask import request, jsonify
from types import SimpleNamespace
from app_runtime import db


def BenchmarkTest76944():
    upload_name = request.files['upload'].filename
    ns = SimpleNamespace(payload=upload_name)
    data = getattr(ns, 'payload')
    if not re.fullmatch('^[\\w\\s.,;:_/\\-=]+$', data):
        return jsonify({'error': 'forbidden'}), 400
    processed = data
    record = db.fetch_one('SELECT * FROM documents WHERE id = ?', (str(processed),))
    return jsonify({'record': str(record)}), 200
