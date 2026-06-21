# SPDX-License-Identifier: Apache-2.0
from markupsafe import Markup
import html
from flask import request


def BenchmarkTest07805():
    ua_value = request.headers.get('User-Agent', '')
    data = str(ua_value).replace('\x00', '')
    processed = html.escape(data)
    return Markup('<img src="' + str(processed) + '">')
