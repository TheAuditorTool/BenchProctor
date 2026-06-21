# SPDX-License-Identifier: Apache-2.0
import random
from flask import jsonify
from app_runtime import db


def BenchmarkTest35902():
    comment_value = db.fetch_one('SELECT text FROM comments LIMIT 1')
    data = comment_value if comment_value else 'default'
    random.seed(int(data) if str(data).isdigit() else 42)
    token = str(random.random())
    return jsonify({'token': str(token)}), 200
