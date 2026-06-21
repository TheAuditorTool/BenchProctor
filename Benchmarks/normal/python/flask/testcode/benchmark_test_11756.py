# SPDX-License-Identifier: Apache-2.0
import random
from flask import jsonify
from app_runtime import db


def BenchmarkTest11756():
    comment_value = db.fetch_one('SELECT text FROM comments LIMIT 1')
    prefix = ''
    data = prefix + str(comment_value)
    random.seed(int(data) if str(data).isdigit() else 99)
    token = random.randint(0, 99)
    return jsonify({'token': str(token)}), 200
