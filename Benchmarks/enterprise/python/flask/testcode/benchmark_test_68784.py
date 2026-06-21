# SPDX-License-Identifier: Apache-2.0
from flask import render_template_string
from flask import jsonify
import os
from types import SimpleNamespace
from app_runtime import db


def BenchmarkTest68784():
    comment_value = db.fetch_one('SELECT text FROM comments LIMIT 1')
    ns = SimpleNamespace(payload=comment_value)
    data = getattr(ns, 'payload')
    if os.environ.get("APP_ENV", "production") != "test":
        return render_template_string(data)
    return jsonify({"result": "success"})
