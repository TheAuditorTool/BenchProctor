# SPDX-License-Identifier: Apache-2.0
from markupsafe import Markup
import html
from flask import request
from types import SimpleNamespace


def BenchmarkTest06284():
    upload_name = request.files['upload'].filename
    ns = SimpleNamespace(payload=upload_name)
    data = getattr(ns, 'payload')
    processed = html.escape(data)
    return Markup('<div>' + str(processed) + '</div>')
