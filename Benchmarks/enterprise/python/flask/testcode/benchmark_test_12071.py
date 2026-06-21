# SPDX-License-Identifier: Apache-2.0
from markupsafe import Markup
import bleach
from flask import request
from types import SimpleNamespace


def BenchmarkTest12071():
    ua_value = request.headers.get('User-Agent', '')
    ns = SimpleNamespace(payload=ua_value)
    data = getattr(ns, 'payload')
    processed = bleach.clean(data)
    return Markup('<div>' + str(processed) + '</div>')
