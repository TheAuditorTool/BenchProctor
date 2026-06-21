# SPDX-License-Identifier: Apache-2.0
import os
from flask import jsonify
from app_runtime import db


def BenchmarkTest33342():
    db_value = db.fetch_one('SELECT name FROM users LIMIT 1')
    base_name = os.path.basename(str(db_value))
    try:
        os.remove('/var/app/data/' + base_name)
    except OSError:
        return jsonify({'error': 'file error'}), 500
    return jsonify({"result": "success"})
