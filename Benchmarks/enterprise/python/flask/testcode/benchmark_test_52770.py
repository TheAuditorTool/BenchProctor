# SPDX-License-Identifier: Apache-2.0
from markupsafe import Markup
from flask import request


def BenchmarkTest52770():
    cookie_value = request.cookies.get('session_token', '')
    data = '{}'.format(cookie_value)
    return Markup('<div>' + str(data) + '</div>')
