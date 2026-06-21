# SPDX-License-Identifier: Apache-2.0
from markupsafe import Markup
import html
from flask import request


def BenchmarkTest32259():
    host_value = request.headers.get('Host', '')
    data = '%s' % (host_value,)
    processed = html.escape(data)
    return Markup('<div>' + str(processed) + '</div>')
