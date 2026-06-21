# SPDX-License-Identifier: Apache-2.0
from flask import jsonify
import os
from app_runtime import db


def BenchmarkTest30137():
    comment_value = db.fetch_one('SELECT text FROM comments LIMIT 1')
    processed = 'true' if str(comment_value).lower() in ('true', '1', 'yes', 'on') else 'false'
    os.environ['APP_USER_PREFERENCE'] = str(processed)
    return jsonify({'config_set': 'APP_USER_PREFERENCE'}), 200
