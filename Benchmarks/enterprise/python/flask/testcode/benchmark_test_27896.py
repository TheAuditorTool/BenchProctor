# SPDX-License-Identifier: Apache-2.0
from markupsafe import Markup
import html
import json
from app_runtime import db


def BenchmarkTest27896():
    comment_value = db.fetch_one('SELECT text FROM comments LIMIT 1')
    try:
        data = json.loads(comment_value).get('value', comment_value)
    except (json.JSONDecodeError, AttributeError):
        data = comment_value
    processed = html.escape(data)
    return Markup('<div>' + str(processed) + '</div>')
