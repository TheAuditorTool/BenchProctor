# SPDX-License-Identifier: Apache-2.0
from markupsafe import Markup
import html
from urllib.parse import unquote
from flask import request


def BenchmarkTest45898():
    referer_value = request.headers.get('Referer', '')
    data = unquote(referer_value)
    processed = html.escape(data)
    return Markup('<div>' + str(processed) + '</div>')
