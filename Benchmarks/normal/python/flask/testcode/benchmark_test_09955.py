# SPDX-License-Identifier: Apache-2.0
from markupsafe import Markup
from flask import request
from types import SimpleNamespace


def BenchmarkTest09955():
    json_value = (request.get_json(silent=True) or {}).get('payload', '')
    ns = SimpleNamespace(payload=json_value)
    data = getattr(ns, 'payload')
    processed = data[:64]
    return Markup('<div>' + str(processed) + '</div>')
