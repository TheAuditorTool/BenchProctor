# SPDX-License-Identifier: Apache-2.0
import random
from flask import jsonify
from types import SimpleNamespace
from app_runtime import db


def BenchmarkTest57602():
    comment_value = db.fetch_one('SELECT text FROM comments LIMIT 1')
    ns = SimpleNamespace(payload=comment_value)
    data = getattr(ns, 'payload')
    random.seed(int(data) if str(data).isdigit() else 1337)
    token = random.randint(0, 100000)
    return jsonify({'token': str(token)}), 200
