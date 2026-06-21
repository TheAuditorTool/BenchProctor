# SPDX-License-Identifier: Apache-2.0
from markupsafe import Markup
import html
from app_runtime import db


def BenchmarkTest26565():
    comment_value = db.fetch_one('SELECT text FROM comments LIMIT 1')
    processed = html.escape(comment_value)
    return Markup('<div>' + str(processed) + '</div>')
