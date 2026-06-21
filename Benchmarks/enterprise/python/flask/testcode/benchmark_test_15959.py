# SPDX-License-Identifier: Apache-2.0
from markupsafe import Markup
from flask import request


def BenchmarkTest15959():
    ua_value = request.headers.get('User-Agent', '')
    data = '%s' % str(ua_value)
    return Markup('<div>' + str(data) + '</div>')
