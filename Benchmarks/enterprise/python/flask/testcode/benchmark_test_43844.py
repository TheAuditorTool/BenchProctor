# SPDX-License-Identifier: Apache-2.0
from markupsafe import Markup
import html
from flask import request


def BenchmarkTest43844():
    origin_value = request.headers.get('Origin', '')
    data = str(origin_value).replace('\x00', '')
    processed = html.escape(data)
    return Markup('<div>' + str(processed) + '</div>')
