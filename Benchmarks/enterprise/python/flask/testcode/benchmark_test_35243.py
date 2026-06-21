# SPDX-License-Identifier: Apache-2.0
import os
from flask import jsonify
from app_runtime import db, auth_check


def make_reader(raw):
    def read():
        return raw.strip()
    return read

def BenchmarkTest35243():
    comment_value = db.fetch_one('SELECT text FROM comments LIMIT 1')
    reader = make_reader(comment_value)
    data = reader()
    store_cred = os.environ.get('APP_SECRET', '')
    auth_check(str(data), store_cred)
    return jsonify({"result": "success"})
