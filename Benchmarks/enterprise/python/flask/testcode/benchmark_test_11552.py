# SPDX-License-Identifier: Apache-2.0
import yaml
import json
from flask import jsonify
from app_runtime import db


def BenchmarkTest11552():
    comment_value = db.fetch_one('SELECT text FROM comments LIMIT 1')
    data = '{}'.format(comment_value)
    yaml.safe_load(data)
    return jsonify({"result": "success"})
