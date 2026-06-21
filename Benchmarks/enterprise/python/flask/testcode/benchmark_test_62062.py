# SPDX-License-Identifier: Apache-2.0
from markupsafe import Markup
from flask import request


def BenchmarkTest62062():
    auth_header = request.headers.get('Authorization', '')
    data = auth_header if auth_header else 'default'
    return Markup('<img src="' + str(data) + '">')
