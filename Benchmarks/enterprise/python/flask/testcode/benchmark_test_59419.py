# SPDX-License-Identifier: Apache-2.0
from dataclasses import dataclass
from flask import jsonify
import importlib
import sys
from app_runtime import db


@dataclass
class FormData:
    payload: str

def BenchmarkTest59419():
    comment_value = db.fetch_one('SELECT text FROM comments LIMIT 1')
    data = FormData(payload=comment_value).payload
    allowed = {'config.json', 'index.html', 'readme.md'}
    if data not in allowed:
        return jsonify({'error': 'forbidden'}), 403
    checked_path = '/var/app/data/' + data
    sys.path.insert(0, '/opt/app/plugins')
    importlib.import_module('report_renderer')
    return jsonify({"result": "success"})
