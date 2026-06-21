# SPDX-License-Identifier: Apache-2.0
from markupsafe import Markup
import html
from flask import request


def BenchmarkTest65526():
    origin_value = request.headers.get('Origin', '')
    data = f'{origin_value:.200s}'
    processed = html.escape(data)
    return Markup('<div>' + str(processed) + '</div>')
