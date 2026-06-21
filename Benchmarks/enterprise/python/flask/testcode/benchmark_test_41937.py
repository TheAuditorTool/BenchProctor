# SPDX-License-Identifier: Apache-2.0
from markupsafe import Markup
from app_runtime import db


def BenchmarkTest41937():
    comment_value = db.fetch_one('SELECT text FROM comments LIMIT 1')
    if comment_value:
        data = comment_value
    else:
        data = ''
    return Markup('<div>' + str(data) + '</div>')
