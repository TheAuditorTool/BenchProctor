# SPDX-License-Identifier: Apache-2.0
from markupsafe import Markup
from flask import request
from types import SimpleNamespace


def BenchmarkTest34867():
    field_value = request.form.get('field', '')
    ns = SimpleNamespace(payload=field_value)
    data = getattr(ns, 'payload')
    processed = data[:64]
    return Markup('<div>' + str(processed) + '</div>')
