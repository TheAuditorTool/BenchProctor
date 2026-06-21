# SPDX-License-Identifier: Apache-2.0
from flask import jsonify
from app_runtime import db


def BenchmarkTest07725():
    comment_value = db.fetch_one('SELECT text FROM comments LIMIT 1')
    data = f'{comment_value:.200s}'
    size = min(int(data) if str(data).isdigit() else 0, 1024)
    data = bytearray(size)
    return jsonify({"result": "success"})
