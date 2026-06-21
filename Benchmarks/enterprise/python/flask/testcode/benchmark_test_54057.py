# SPDX-License-Identifier: Apache-2.0
from markupsafe import Markup
from flask import request


def BenchmarkTest54057():
    auth_header = request.headers.get('Authorization', '')
    parts = str(auth_header).split(',')
    data = ','.join(parts)
    return Markup('<img src="' + str(data) + '">')
