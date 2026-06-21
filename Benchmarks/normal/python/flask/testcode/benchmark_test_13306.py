# SPDX-License-Identifier: Apache-2.0
from flask import jsonify
import os
from app_runtime import db


def make_reader(raw):
    def read():
        return raw.strip()
    return read

def BenchmarkTest13306():
    comment_value = db.fetch_one('SELECT text FROM comments LIMIT 1')
    reader = make_reader(comment_value)
    data = reader()
    processed = 'true' if str(data).lower() in ('true', '1', 'yes', 'on') else 'false'
    os.environ['APP_USER_PREFERENCE'] = str(processed)
    return jsonify({'config_set': 'APP_USER_PREFERENCE'}), 200
