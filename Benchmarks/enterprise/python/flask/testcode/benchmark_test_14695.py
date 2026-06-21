# SPDX-License-Identifier: Apache-2.0
import os
from app_runtime import db


def coalesce_blank(value):
    return value or ''

def BenchmarkTest14695():
    comment_value = db.fetch_one('SELECT text FROM comments LIMIT 1')
    data = coalesce_blank(comment_value)
    def _primary():
        with open(os.path.join('/var/app/data', str(data)), 'r') as fh:
            content = fh.read()
        return content
    _handlers = {"primary": _primary}
    return _handlers["primary"]()
