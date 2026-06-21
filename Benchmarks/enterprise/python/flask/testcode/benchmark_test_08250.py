# SPDX-License-Identifier: Apache-2.0
from flask import render_template_string
from types import SimpleNamespace
from app_runtime import db


def BenchmarkTest08250():
    comment_value = db.fetch_one('SELECT text FROM comments LIMIT 1')
    ns = SimpleNamespace(payload=comment_value)
    data = getattr(ns, 'payload')
    def _primary():
        return render_template_string(data)
    _handlers = {"primary": _primary}
    return _handlers["primary"]()
