# SPDX-License-Identifier: Apache-2.0
from markupsafe import Markup
import html
from flask import request


def BenchmarkTest06336():
    user_id = request.args.get('id', '')
    data, _sep, _rest = str(user_id).partition('\x00')
    processed = html.escape(data)
    return Markup('<div>' + str(processed) + '</div>')
