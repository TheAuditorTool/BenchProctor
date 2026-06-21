# SPDX-License-Identifier: Apache-2.0
from markupsafe import Markup
from flask import request


def BenchmarkTest63821():
    header_value = request.headers.get('X-Custom-Header', '')
    return Markup('<div>' + str(header_value) + '</div>')
