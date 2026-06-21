# SPDX-License-Identifier: Apache-2.0
from markupsafe import Markup
from flask import request
from types import SimpleNamespace


def BenchmarkTest20583():
    referer_value = request.headers.get('Referer', '')
    ns = SimpleNamespace(payload=referer_value)
    data = getattr(ns, 'payload')
    processed = data[:64]
    return Markup('<div>' + str(processed) + '</div>')
