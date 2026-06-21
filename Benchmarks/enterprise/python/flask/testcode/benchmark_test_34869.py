# SPDX-License-Identifier: Apache-2.0
from markupsafe import Markup
import html
from flask import request


def BenchmarkTest34869():
    ua_value = request.headers.get('User-Agent', '')
    data = ' '.join(str(ua_value).split())
    processed = html.escape(data)
    return Markup('<div>' + str(processed) + '</div>')
