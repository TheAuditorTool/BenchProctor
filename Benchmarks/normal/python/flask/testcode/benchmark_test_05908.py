# SPDX-License-Identifier: Apache-2.0
from markupsafe import Markup
import html
from flask import request


def BenchmarkTest05908():
    origin_value = request.headers.get('Origin', '')
    data = '%s' % str(origin_value)
    processed = html.escape(data)
    return Markup('<div>' + str(processed) + '</div>')
