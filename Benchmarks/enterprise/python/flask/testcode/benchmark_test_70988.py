# SPDX-License-Identifier: Apache-2.0
from markupsafe import Markup
import html
from flask import request


def BenchmarkTest70988():
    user_id = request.args.get('id', '')
    data = (lambda v: v.strip())(user_id)
    processed = html.escape(data)
    return Markup('<div>' + str(processed) + '</div>')
