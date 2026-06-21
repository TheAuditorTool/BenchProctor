# SPDX-License-Identifier: Apache-2.0
from flask import jsonify
import os
from types import SimpleNamespace
from app_runtime import db


def BenchmarkTest70961():
    comment_value = db.fetch_one('SELECT text FROM comments LIMIT 1')
    ns = SimpleNamespace(payload=comment_value)
    data = getattr(ns, 'payload')
    os.environ['APP_USER_PREFERENCE'] = str(data)
    return jsonify({'config_set': 'APP_USER_PREFERENCE'}), 200
