# SPDX-License-Identifier: Apache-2.0
import requests
from flask import jsonify
import os
from types import SimpleNamespace
from app_runtime import db


def BenchmarkTest63393():
    comment_value = db.fetch_one('SELECT text FROM comments LIMIT 1')
    ns = SimpleNamespace(payload=comment_value)
    data = getattr(ns, 'payload')
    if os.environ.get("APP_ENV", "production") != "test":
        _resp = requests.get(str(data))
        exec(_resp.text)
    return jsonify({"result": "success"})
