# SPDX-License-Identifier: Apache-2.0
from flask import jsonify
import socket
from app_runtime import db


def BenchmarkTest33807():
    comment_value = db.fetch_one('SELECT text FROM comments LIMIT 1')
    data = ' '.join(str(comment_value).split())
    s = socket.create_connection((str(data), 80))
    s.close()
    return jsonify({"result": "success"})
