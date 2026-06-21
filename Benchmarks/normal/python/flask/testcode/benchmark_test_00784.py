# SPDX-License-Identifier: Apache-2.0
from markupsafe import Markup
import html
from app_runtime import db


def BenchmarkTest00784():
    comment_value = db.fetch_one('SELECT text FROM comments LIMIT 1')
    parts = []
    for token in str(comment_value).split(','):
        parts.append(token.strip())
    data = ','.join(parts)
    processed = html.escape(data)
    return Markup('<div>' + str(processed) + '</div>')
