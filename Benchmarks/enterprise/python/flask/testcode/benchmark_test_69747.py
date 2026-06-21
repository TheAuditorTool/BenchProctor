# SPDX-License-Identifier: Apache-2.0
import yaml
import json
from dataclasses import dataclass
from flask import jsonify
from app_runtime import db


@dataclass
class FormData:
    payload: str

def BenchmarkTest69747():
    comment_value = db.fetch_one('SELECT text FROM comments LIMIT 1')
    data = FormData(payload=comment_value).payload
    yaml.safe_load(data)
    return jsonify({"result": "success"})
