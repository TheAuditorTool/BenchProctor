# SPDX-License-Identifier: Apache-2.0
from markupsafe import Markup
from flask import request


def BenchmarkTest62646():
    header_value = request.headers.get('X-Custom-Header', '')
    data = header_value if header_value else 'default'
    return Markup('<img src="' + str(data) + '">')
