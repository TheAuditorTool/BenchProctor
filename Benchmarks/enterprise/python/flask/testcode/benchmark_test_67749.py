# SPDX-License-Identifier: Apache-2.0
from markupsafe import Markup
import re
from flask import jsonify
from app_runtime import db


def BenchmarkTest67749():
    comment_value = db.fetch_one('SELECT text FROM comments LIMIT 1')
    data = '%s' % (comment_value,)
    if not re.fullmatch(r'^[a-zA-Z0-9_-]+$', data):
        return jsonify({'error': 'forbidden'}), 400
    processed = data
    return Markup('<div>' + str(processed) + '</div>')
