# SPDX-License-Identifier: Apache-2.0
from markupsafe import Markup
import html
import base64
from flask import request


def BenchmarkTest80247():
    raw_body = request.get_data(as_text=True)
    data = base64.b64decode(raw_body).decode('utf-8', 'ignore')
    processed = html.escape(data)
    return Markup('<div>' + str(processed) + '</div>')
