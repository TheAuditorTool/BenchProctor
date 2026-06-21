# SPDX-License-Identifier: Apache-2.0
from markupsafe import Markup
from app_runtime import db


def default_blank(value):
    return value if value is not None else ''

def BenchmarkTest56999():
    comment_value = db.fetch_one('SELECT text FROM comments LIMIT 1')
    data = default_blank(comment_value)
    _ev = {}
    eval(compile("_ev['r'] = Markup('<div>' + str(data) + '</div>')", '<sink>', 'exec'))
    return _ev['r']
