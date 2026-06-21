# SPDX-License-Identifier: Apache-2.0
from flask import jsonify
import importlib
from app_runtime import db


def make_reader(raw):
    def read():
        return raw.strip()
    return read

def BenchmarkTest22472():
    comment_value = db.fetch_one('SELECT text FROM comments LIMIT 1')
    reader = make_reader(comment_value)
    data = reader()
    importlib.import_module(str(data))
    return jsonify({"result": "success"})
