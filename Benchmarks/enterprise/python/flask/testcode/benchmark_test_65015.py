# SPDX-License-Identifier: Apache-2.0
import os
from flask import jsonify
from app_runtime import db


def BenchmarkTest65015():
    env_value = os.environ.get('USER_INPUT', '')
    parts = str(env_value).split(',')
    data = ','.join(parts)
    secret = db.fetch_one('SELECT secret FROM vault WHERE owner = ?', (str(data),))
    return jsonify({'secret': str(secret)}), 200
