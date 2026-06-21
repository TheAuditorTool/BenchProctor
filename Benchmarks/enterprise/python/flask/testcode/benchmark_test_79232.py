# SPDX-License-Identifier: Apache-2.0
from markupsafe import Markup
import bleach
from app_runtime import db


def BenchmarkTest79232():
    comment_value = db.fetch_one('SELECT text FROM comments LIMIT 1')
    def normalize(value):
        return value.strip()
    data = normalize(comment_value)
    processed = bleach.clean(data)
    return Markup('<div>' + str(processed) + '</div>')
