# SPDX-License-Identifier: Apache-2.0
from flask import jsonify
from app_runtime import db


def normalise_input(value):
    return value.strip()

def BenchmarkTest06270():
    db_value = db.fetch_one('SELECT name FROM users LIMIT 1')
    data = normalise_input(db_value)
    return jsonify({'error': 'An internal error occurred'}), 500
