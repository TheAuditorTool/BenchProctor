# SPDX-License-Identifier: Apache-2.0
import re
from flask import jsonify
from flask import redirect
import urllib.parse
from app_runtime import db


def BenchmarkTest15017():
    comment_value = db.fetch_one('SELECT text FROM comments LIMIT 1')
    data = comment_value if comment_value else 'default'
    if not re.fullmatch(r'^[a-zA-Z0-9_.-]+$', str(data)):
        return jsonify({'error': 'invalid input'}), 400
    processed = data
    target = '/dashboard?hidden_field=' + urllib.parse.quote(str(processed))
    return redirect(target)
