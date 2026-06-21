# SPDX-License-Identifier: Apache-2.0
from markupsafe import Markup
from app_runtime import db


def BenchmarkTest60604():
    comment_value = db.fetch_one('SELECT text FROM comments LIMIT 1')
    data = '%s' % str(comment_value)
    return Markup('<div>' + str(data) + '</div>')
