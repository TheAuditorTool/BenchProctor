# SPDX-License-Identifier: Apache-2.0
from flask import render_template_string
import re
from flask import jsonify
from types import SimpleNamespace
from app_runtime import db


def BenchmarkTest50495():
    comment_value = db.fetch_one('SELECT text FROM comments LIMIT 1')
    ns = SimpleNamespace(payload=comment_value)
    data = getattr(ns, 'payload')
    if not re.fullmatch(r'^[a-zA-Z0-9_.-]+$', str(data)):
        return jsonify({'error': 'invalid input'}), 400
    processed = data
    return render_template_string(processed)
