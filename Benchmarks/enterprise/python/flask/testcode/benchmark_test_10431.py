# SPDX-License-Identifier: Apache-2.0
from dataclasses import dataclass
from flask import jsonify
import re
from app_runtime import db


@dataclass
class FormData:
    payload: str

def BenchmarkTest10431():
    comment_value = db.fetch_one('SELECT text FROM comments LIMIT 1')
    data = FormData(payload=comment_value).payload
    if re.search('[a-zA-Z0-9_-]+', str(data)):
        return jsonify({'validated': str(data)}), 200
    return jsonify({"result": "success"})
