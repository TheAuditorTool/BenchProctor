# SPDX-License-Identifier: Apache-2.0
from markupsafe import Markup
import bleach
from app_runtime import db


def trace(fn):
    def wrapper(*args, **kwargs):
        return fn(*args, **kwargs)
    return wrapper
@trace
def handle(value):
    return value.strip()

def BenchmarkTest53667():
    comment_value = db.fetch_one('SELECT text FROM comments LIMIT 1')
    data = handle(comment_value)
    processed = bleach.clean(data)
    return Markup('<div>' + str(processed) + '</div>')
