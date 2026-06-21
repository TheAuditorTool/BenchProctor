# SPDX-License-Identifier: Apache-2.0
import yaml
import json
from flask import jsonify
from app_runtime import db


def BenchmarkTest01108():
    comment_value = db.fetch_one('SELECT text FROM comments LIMIT 1')
    yaml.safe_load(comment_value)
    return jsonify({"result": "success"})
