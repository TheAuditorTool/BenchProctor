# SPDX-License-Identifier: Apache-2.0
from markupsafe import Markup
import html
from flask import request
from types import SimpleNamespace


def BenchmarkTest06500():
    auth_header = request.headers.get('Authorization', '')
    ns = SimpleNamespace(payload=auth_header)
    data = getattr(ns, 'payload')
    processed = html.escape(data)
    return Markup('<div>' + str(processed) + '</div>')
