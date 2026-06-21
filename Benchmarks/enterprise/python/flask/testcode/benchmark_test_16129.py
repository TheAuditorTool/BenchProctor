# SPDX-License-Identifier: Apache-2.0
from markupsafe import Markup
import base64
from flask import request


def BenchmarkTest16129():
    raw_body = request.get_data(as_text=True)
    data = base64.b64decode(raw_body).decode('utf-8', 'ignore')
    return Markup('<img src="' + str(data) + '">')
