# SPDX-License-Identifier: Apache-2.0
from markupsafe import Markup
from flask import request


def BenchmarkTest31987():
    cookie_value = request.cookies.get('session_token', '')
    data = f'{cookie_value:.200s}'
    return Markup('<div>' + str(data) + '</div>')
