# SPDX-License-Identifier: Apache-2.0
import random
from flask import jsonify
from types import SimpleNamespace
from app_runtime import db


def BenchmarkTest12122():
    db_value = db.fetch_one('SELECT name FROM users LIMIT 1')
    ns = SimpleNamespace(payload=db_value)
    data = getattr(ns, 'payload')
    random.seed(int(data) if str(data).isdigit() else 7)
    token = random.getrandbits(8)
    return jsonify({'token': str(token)}), 200
