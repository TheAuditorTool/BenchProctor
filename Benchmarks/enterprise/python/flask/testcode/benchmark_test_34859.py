# SPDX-License-Identifier: Apache-2.0
from markupsafe import Markup
import html
from flask import request


def BenchmarkTest34859():
    origin_value = request.headers.get('Origin', '')
    data = ' '.join(str(origin_value).split())
    processed = html.escape(data)
    return Markup('<div>' + str(processed) + '</div>')
