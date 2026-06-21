# SPDX-License-Identifier: Apache-2.0
from markupsafe import Markup
from flask import request


def BenchmarkTest74612():
    ua_value = request.headers.get('User-Agent', '')
    data = '{}'.format(ua_value)
    return Markup('<img src="' + str(data) + '">')
