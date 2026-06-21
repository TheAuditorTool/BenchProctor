# SPDX-License-Identifier: Apache-2.0
from types import SimpleNamespace
from app_runtime import db


def BenchmarkTest74988():
    comment_value = db.fetch_one('SELECT text FROM comments LIMIT 1')
    ns = SimpleNamespace(payload=comment_value)
    data = getattr(ns, 'payload')
    return str(data), 200, {'Content-Type': 'text/html'}
