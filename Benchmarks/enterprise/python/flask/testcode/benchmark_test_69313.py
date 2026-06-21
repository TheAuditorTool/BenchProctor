# SPDX-License-Identifier: Apache-2.0
import os
from flask import jsonify
import importlib
import sys
from app_runtime import db


def coalesce_blank(value):
    return value or ''

def BenchmarkTest69313():
    db_value = db.fetch_one('SELECT name FROM users LIMIT 1')
    data = coalesce_blank(db_value)
    base_dir = '/var/app/data'
    full_path = os.path.realpath(os.path.join(base_dir, data))
    if not full_path.startswith(base_dir + os.sep):
        return jsonify({'error': 'forbidden'}), 403
    checked_path = full_path
    sys.path.insert(0, '/opt/app/plugins')
    importlib.import_module('report_renderer')
    return jsonify({"result": "success"})
