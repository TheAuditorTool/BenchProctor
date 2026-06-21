# SPDX-License-Identifier: Apache-2.0
import yaml
from flask import jsonify
from app_runtime import db


def BenchmarkTest06458():
    comment_value = db.fetch_one('SELECT text FROM comments LIMIT 1')
    data = f'{comment_value:.200s}'
    yaml.load(data, Loader=yaml.UnsafeLoader)
    return jsonify({"result": "success"})
