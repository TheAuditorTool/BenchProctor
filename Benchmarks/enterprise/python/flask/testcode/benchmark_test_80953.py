# SPDX-License-Identifier: Apache-2.0
import requests
import re
from flask import request, jsonify
from types import SimpleNamespace
from app_runtime import db


def BenchmarkTest80953():
    user_id = request.args.get('id', '')
    ns = SimpleNamespace(payload=user_id)
    data = getattr(ns, 'payload')
    if not re.match(r'^.{1,256}$', str(data)):
        return jsonify({'error': 'schema invalid'}), 400
    _resp = requests.get(str(data))
    db.execute('INSERT INTO feed (data) VALUES (?)', (_resp.text,))
    return jsonify({"result": "success"})
