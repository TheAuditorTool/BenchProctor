# SPDX-License-Identifier: Apache-2.0
from markupsafe import Markup
import html
from flask import request
from types import SimpleNamespace


def BenchmarkTest67752():
    cookie_value = request.cookies.get('session_token', '')
    ns = SimpleNamespace(payload=cookie_value)
    data = getattr(ns, 'payload')
    processed = html.escape(data)
    return Markup('<div>' + str(processed) + '</div>')
