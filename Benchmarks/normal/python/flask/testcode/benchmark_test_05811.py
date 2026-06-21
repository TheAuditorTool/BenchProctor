# SPDX-License-Identifier: Apache-2.0
from markupsafe import Markup
import html
from flask import request


def BenchmarkTest05811():
    user_id = request.args.get('id', '')
    if user_id:
        data = user_id
    else:
        data = ''
    processed = html.escape(data)
    return Markup('<div>' + str(processed) + '</div>')
