# SPDX-License-Identifier: Apache-2.0
import unicodedata
from app_runtime import db


def BenchmarkTest61824():
    comment_value = db.fetch_one('SELECT text FROM comments LIMIT 1')
    data = (lambda v: v.strip())(comment_value)
    normalized = unicodedata.normalize('NFKC', str(data))
    return '<p>' + normalized + '</p>', 200, {'Content-Type': 'text/html'}
