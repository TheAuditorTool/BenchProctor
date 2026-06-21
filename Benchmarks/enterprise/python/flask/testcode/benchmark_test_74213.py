# SPDX-License-Identifier: Apache-2.0
from markupsafe import Markup
from flask import request


def BenchmarkTest74213():
    auth_header = request.headers.get('Authorization', '')
    data = auth_header if auth_header else 'default'
    return Markup('<div>' + str(data) + '</div>')
