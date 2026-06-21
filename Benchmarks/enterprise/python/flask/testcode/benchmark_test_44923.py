# SPDX-License-Identifier: Apache-2.0
from markupsafe import Markup
from flask import request


def BenchmarkTest44923():
    origin_value = request.headers.get('Origin', '')
    data = origin_value if origin_value else 'default'
    return Markup('<div>' + str(data) + '</div>')
