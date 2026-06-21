# SPDX-License-Identifier: Apache-2.0
from markupsafe import Markup
from flask import request


def BenchmarkTest79516():
    header_value = request.headers.get('X-Custom-Header', '')
    data = '%s' % str(header_value)
    return Markup('<div>' + str(data) + '</div>')
