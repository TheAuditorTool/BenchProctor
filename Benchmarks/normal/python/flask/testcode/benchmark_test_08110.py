# SPDX-License-Identifier: Apache-2.0
from markupsafe import Markup
from flask import request


def BenchmarkTest08110():
    ua_value = request.headers.get('User-Agent', '')
    data = ua_value if ua_value else 'default'
    return Markup('<div>' + str(data) + '</div>')
