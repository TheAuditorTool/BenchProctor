# SPDX-License-Identifier: Apache-2.0
from markupsafe import Markup
import html
from flask import request


def BenchmarkTest01566():
    raw_body = request.get_data(as_text=True)
    data = (lambda v: v.strip())(raw_body)
    processed = html.escape(data)
    return Markup('<div>' + str(processed) + '</div>')
