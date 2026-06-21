# SPDX-License-Identifier: Apache-2.0
from markupsafe import Markup
from flask import request


def BenchmarkTest78369():
    auth_header = request.headers.get('Authorization', '')
    data = f'{auth_header}'
    return Markup('<div>' + str(data) + '</div>')
