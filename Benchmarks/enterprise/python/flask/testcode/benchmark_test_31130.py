# SPDX-License-Identifier: Apache-2.0
from markupsafe import Markup
import html
from flask import request


def BenchmarkTest31130():
    referer_value = request.headers.get('Referer', '')
    collected = None
    def on_input(value):
        nonlocal collected
        collected = value
    on_input(referer_value)
    data = collected
    processed = str(data).replace("<script", "")
    return Markup('<div>' + str(processed) + '</div>')
