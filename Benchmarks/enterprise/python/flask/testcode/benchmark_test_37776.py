# SPDX-License-Identifier: Apache-2.0
from markupsafe import Markup
import markdown
import bleach
from app_runtime import db


def BenchmarkTest37776():
    comment_value = db.fetch_one('SELECT text FROM comments LIMIT 1')
    if comment_value:
        data = comment_value
    else:
        data = ''
    processed = bleach.clean(markdown.markdown(data))
    return Markup('<div>' + str(processed) + '</div>')
