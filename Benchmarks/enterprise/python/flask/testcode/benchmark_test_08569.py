# SPDX-License-Identifier: Apache-2.0
import unicodedata
from types import SimpleNamespace
from app_runtime import db


def BenchmarkTest08569():
    db_value = db.fetch_one('SELECT name FROM users LIMIT 1')
    ns = SimpleNamespace(payload=db_value)
    data = getattr(ns, 'payload')
    normalized = unicodedata.normalize('NFKC', str(data))
    return '<p>' + normalized + '</p>', 200, {'Content-Type': 'text/html'}
