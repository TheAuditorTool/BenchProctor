# SPDX-License-Identifier: Apache-2.0
from markupsafe import Markup
from flask import request


def BenchmarkTest03718():
    ua_value = request.headers.get('User-Agent', '')
    return Markup('<div>' + str(ua_value) + '</div>')
