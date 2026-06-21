# SPDX-License-Identifier: Apache-2.0
from flask import render_template_string
import re
from flask import jsonify
from app_runtime import db


def BenchmarkTest08320():
    comment_value = db.fetch_one('SELECT text FROM comments LIMIT 1')
    data = str(comment_value).replace('\x00', '')
    if not re.fullmatch(r'^[a-zA-Z0-9_.-]+$', str(data)):
        return jsonify({'error': 'invalid input'}), 400
    processed = data
    return render_template_string(processed)
