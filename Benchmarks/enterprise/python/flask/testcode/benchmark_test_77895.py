# SPDX-License-Identifier: Apache-2.0
from markupsafe import Markup
import html
from flask import request
from types import SimpleNamespace


def BenchmarkTest77895():
    user_id = request.args.get('id', '')
    ns = SimpleNamespace(payload=user_id)
    data = getattr(ns, 'payload')
    processed = html.escape(data)
    return Markup('<div>' + str(processed) + '</div>')
