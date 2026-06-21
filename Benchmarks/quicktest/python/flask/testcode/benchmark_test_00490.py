# SPDX-License-Identifier: Apache-2.0
from dataclasses import dataclass
from flask import jsonify
import importlib
from app_runtime import db


@dataclass
class FormData:
    payload: str

def BenchmarkTest00490():
    comment_value = db.fetch_one('SELECT text FROM comments LIMIT 1')
    data = FormData(payload=comment_value).payload
    if data not in ('asc', 'desc', 'name', 'created'):
        return jsonify({'error': 'forbidden'}), 400
    processed = data
    importlib.import_module(str(processed))
    return jsonify({"result": "success"})
