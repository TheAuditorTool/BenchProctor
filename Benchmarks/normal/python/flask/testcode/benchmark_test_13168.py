# SPDX-License-Identifier: Apache-2.0
from markupsafe import Markup
import bleach
from flask import request
from types import SimpleNamespace


def BenchmarkTest13168():
    referer_value = request.headers.get('Referer', '')
    ns = SimpleNamespace(payload=referer_value)
    data = getattr(ns, 'payload')
    processed = bleach.clean(data)
    return Markup('<div>' + str(processed) + '</div>')
