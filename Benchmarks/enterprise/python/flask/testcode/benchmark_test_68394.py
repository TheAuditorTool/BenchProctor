# SPDX-License-Identifier: Apache-2.0
from markupsafe import Markup
import html
from types import SimpleNamespace
from app_runtime import db


def BenchmarkTest68394():
    db_value = db.fetch_one('SELECT name FROM users LIMIT 1')
    ns = SimpleNamespace(payload=db_value)
    data = getattr(ns, 'payload')
    processed = html.escape(data)
    return Markup('<div>' + str(processed) + '</div>')
