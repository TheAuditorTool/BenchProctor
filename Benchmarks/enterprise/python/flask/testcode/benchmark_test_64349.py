# SPDX-License-Identifier: Apache-2.0
from markupsafe import Markup
from flask import request


def BenchmarkTest64349():
    ua_value = request.headers.get('User-Agent', '')
    data = ' '.join(str(ua_value).split())
    return Markup('<div>' + str(data) + '</div>')
