# SPDX-License-Identifier: Apache-2.0
from markupsafe import Markup
import bleach
from flask import request
from types import SimpleNamespace


def BenchmarkTest25953():
    raw_body = request.get_data(as_text=True)
    ns = SimpleNamespace(payload=raw_body)
    data = getattr(ns, 'payload')
    processed = bleach.clean(data)
    return Markup('<div>' + str(processed) + '</div>')
