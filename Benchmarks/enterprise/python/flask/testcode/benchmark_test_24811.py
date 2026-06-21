# SPDX-License-Identifier: Apache-2.0
import requests
from app_runtime import db


def coalesce_blank(value):
    return value or ''

def BenchmarkTest24811():
    comment_value = db.fetch_one('SELECT text FROM comments LIMIT 1')
    data = coalesce_blank(comment_value)
    def _primary():
        return '<script src="' + str(data) + '"></script>', 200, {'Content-Type': 'text/html'}
    _handlers = {"primary": _primary}
    return _handlers["primary"]()
