# SPDX-License-Identifier: Apache-2.0
from flask import jsonify
import os
from app_runtime import db


def BenchmarkTest12481():
    comment_value = db.fetch_one('SELECT text FROM comments LIMIT 1')
    data = (lambda v: v.strip())(comment_value)
    os.environ['APP_USER_PREFERENCE'] = str(data)
    return jsonify({'config_set': 'APP_USER_PREFERENCE'}), 200
