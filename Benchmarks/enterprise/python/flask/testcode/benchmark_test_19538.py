# SPDX-License-Identifier: Apache-2.0
from markupsafe import Markup
import html
from flask import request


def BenchmarkTest19538():
    raw_body = request.get_data(as_text=True)
    data = raw_body if raw_body else 'default'
    processed = html.escape(data)
    return Markup('<div>' + str(processed) + '</div>')
