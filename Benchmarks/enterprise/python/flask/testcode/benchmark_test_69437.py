# SPDX-License-Identifier: Apache-2.0
from app_runtime import db


def BenchmarkTest69437():
    comment_value = db.fetch_one('SELECT text FROM comments LIMIT 1')
    collected = None
    def on_input(value):
        nonlocal collected
        collected = value
    on_input(comment_value)
    data = collected
    return '<html><body><h1>' + str(data) + '</h1></body></html>', 200, {'Content-Type': 'text/html'}
