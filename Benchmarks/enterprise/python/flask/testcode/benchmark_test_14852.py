# SPDX-License-Identifier: Apache-2.0
from markupsafe import Markup
import base64
from flask import request


def BenchmarkTest14852():
    auth_header = request.headers.get('Authorization', '')
    data = base64.b64decode(auth_header).decode('utf-8', 'ignore')
    return Markup('<div>' + str(data) + '</div>')
