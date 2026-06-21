# SPDX-License-Identifier: Apache-2.0
from flask import jsonify
import defusedxml.ElementTree
from app_runtime import db


def BenchmarkTest08021():
    comment_value = db.fetch_one('SELECT text FROM comments LIMIT 1')
    defusedxml.ElementTree.fromstring(str(comment_value))
    return jsonify({"result": "success"})
