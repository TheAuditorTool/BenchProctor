# SPDX-License-Identifier: Apache-2.0
from markupsafe import Markup
import html
from urllib.parse import unquote
from flask import request


def BenchmarkTest01189():
    user_id = request.args.get('id', '')
    data = unquote(user_id)
    processed = html.escape(data)
    return Markup('<div>' + str(processed) + '</div>')
