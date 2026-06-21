# SPDX-License-Identifier: Apache-2.0
from markupsafe import Markup
import html
from flask import request


def BenchmarkTest64225():
    raw_body = request.get_data(as_text=True)
    data = ' '.join(str(raw_body).split())
    processed = html.escape(data)
    return Markup('<div>' + str(processed) + '</div>')
