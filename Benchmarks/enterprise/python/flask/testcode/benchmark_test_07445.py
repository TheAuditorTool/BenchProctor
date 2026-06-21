# SPDX-License-Identifier: Apache-2.0
from markupsafe import Markup
import json
from app_runtime import db


def BenchmarkTest07445():
    comment_value = db.fetch_one('SELECT text FROM comments LIMIT 1')
    try:
        data = json.loads(comment_value).get('value', comment_value)
    except (json.JSONDecodeError, AttributeError):
        data = comment_value
    return Markup('<div>' + str(data) + '</div>')
