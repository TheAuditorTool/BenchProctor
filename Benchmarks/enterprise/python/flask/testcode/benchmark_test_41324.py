# SPDX-License-Identifier: Apache-2.0
from markupsafe import Markup
import html
from flask import request


def BenchmarkTest41324():
    referer_value = request.headers.get('Referer', '')
    data = (lambda v: v.strip())(referer_value)
    processed = html.escape(data)
    return Markup('<div>' + str(processed) + '</div>')
