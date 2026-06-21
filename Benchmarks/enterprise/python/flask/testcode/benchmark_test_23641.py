# SPDX-License-Identifier: Apache-2.0
from markupsafe import Markup
from flask import request


def BenchmarkTest23641():
    header_value = request.headers.get('X-Custom-Header', '')
    data = f'{header_value}'
    return Markup('<div>' + str(data) + '</div>')
