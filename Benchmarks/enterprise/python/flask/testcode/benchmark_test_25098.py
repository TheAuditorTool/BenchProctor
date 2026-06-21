# SPDX-License-Identifier: Apache-2.0
from flask import jsonify
import os
from app_runtime import db


def BenchmarkTest25098():
    db_value = db.fetch_one('SELECT name FROM users LIMIT 1')
    data = db_value if db_value else 'default'
    os.environ['APP_USER_PREFERENCE'] = str(data)
    return jsonify({'config_set': 'APP_USER_PREFERENCE'}), 200
