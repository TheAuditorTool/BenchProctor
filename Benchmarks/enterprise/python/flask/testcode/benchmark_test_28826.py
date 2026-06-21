# SPDX-License-Identifier: Apache-2.0
from markupsafe import Markup
from flask import request


def BenchmarkTest28826():
    header_value = request.headers.get('X-Custom-Header', '')
    data = f'{header_value:.200s}'
    return Markup('<div>' + str(data) + '</div>')
