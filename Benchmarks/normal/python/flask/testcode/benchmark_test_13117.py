# SPDX-License-Identifier: Apache-2.0
from markupsafe import Markup
import html
from flask import request


def BenchmarkTest13117():
    ua_value = request.headers.get('User-Agent', '')
    data = '%s' % str(ua_value)
    processed = html.escape(data)
    return Markup('<div>' + str(processed) + '</div>')
