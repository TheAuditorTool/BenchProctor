# SPDX-License-Identifier: Apache-2.0
from flask import jsonify
import os
from app_runtime import db


def make_reader(raw):
    def read():
        return raw.strip()
    return read

def BenchmarkTest15712():
    comment_value = db.fetch_one('SELECT text FROM comments LIMIT 1')
    reader = make_reader(comment_value)
    data = reader()
    entries = os.listdir(str(data))
    return jsonify({'listing': entries}), 200
