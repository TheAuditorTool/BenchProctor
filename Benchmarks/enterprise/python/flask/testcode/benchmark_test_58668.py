# SPDX-License-Identifier: Apache-2.0
from markupsafe import Markup
import html
from flask import request


def BenchmarkTest58668():
    user_id = request.args.get('id', '')
    data = '%s' % str(user_id)
    processed = html.escape(data)
    return Markup('<div>' + str(processed) + '</div>')
