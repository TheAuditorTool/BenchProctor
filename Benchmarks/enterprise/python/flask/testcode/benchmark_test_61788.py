# SPDX-License-Identifier: Apache-2.0
from markupsafe import Markup
import html
from flask import request


def BenchmarkTest61788():
    raw_body = request.get_data(as_text=True)
    data = '{}'.format(raw_body)
    processed = html.escape(data)
    return Markup('<div>' + str(processed) + '</div>')
