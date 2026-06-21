# SPDX-License-Identifier: Apache-2.0
from markupsafe import Markup
from flask import request


def BenchmarkTest56255():
    ua_value = request.headers.get('User-Agent', '')
    return Markup('<img src="' + str(ua_value) + '">')
