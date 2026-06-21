# SPDX-License-Identifier: Apache-2.0
from markupsafe import Markup
import html
from types import SimpleNamespace
from app_runtime import db


def BenchmarkTest55547():
    comment_value = db.fetch_one('SELECT text FROM comments LIMIT 1')
    ns = SimpleNamespace(payload=comment_value)
    data = getattr(ns, 'payload')
    processed = html.escape(data)
    return Markup('<div>' + str(processed) + '</div>')
