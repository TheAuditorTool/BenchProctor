# SPDX-License-Identifier: Apache-2.0
import random
from flask import jsonify
from app_runtime import db


def BenchmarkTest67126():
    comment_value = db.fetch_one('SELECT text FROM comments LIMIT 1')
    random.seed(int(comment_value) if str(comment_value).isdigit() else 1337)
    token = random.randint(0, 100000)
    return jsonify({'token': str(token)}), 200
