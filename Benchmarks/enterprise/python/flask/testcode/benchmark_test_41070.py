# SPDX-License-Identifier: Apache-2.0
from markupsafe import Markup
import base64
from flask import request


def BenchmarkTest41070():
    cookie_value = request.cookies.get('session_token', '')
    data = base64.b64decode(cookie_value).decode('utf-8', 'ignore')
    return Markup('<img src="' + str(data) + '">')
