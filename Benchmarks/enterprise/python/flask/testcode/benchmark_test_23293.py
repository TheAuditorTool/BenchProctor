# SPDX-License-Identifier: Apache-2.0
from markupsafe import Markup
import html
from flask import request
from types import SimpleNamespace


def BenchmarkTest23293():
    multipart_value = request.form.get('multipart_field', '')
    ns = SimpleNamespace(payload=multipart_value)
    data = getattr(ns, 'payload')
    processed = str(data).replace("<script", "")
    return Markup('<div>' + str(processed) + '</div>')
