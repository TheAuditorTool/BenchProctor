# SPDX-License-Identifier: Apache-2.0
from markupsafe import Markup
from flask import request


def BenchmarkTest58257():
    ua_value = request.headers.get('User-Agent', '')
    data = ua_value if ua_value else 'default'
    return Markup('<div>' + str(data) + '</div>')
