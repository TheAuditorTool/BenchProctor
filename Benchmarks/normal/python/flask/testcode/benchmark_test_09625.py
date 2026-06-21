# SPDX-License-Identifier: Apache-2.0
from markupsafe import Markup
import html
from flask import request


def BenchmarkTest09625():
    origin_value = request.headers.get('Origin', '')
    prefix = ''
    data = prefix + str(origin_value)
    processed = html.escape(data)
    return Markup('<img src="' + str(processed) + '">')
