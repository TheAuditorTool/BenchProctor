# SPDX-License-Identifier: Apache-2.0
from markupsafe import Markup
from flask import request


def BenchmarkTest15650():
    auth_header = request.headers.get('Authorization', '')
    data = f'{auth_header:.200s}'
    return Markup('<div>' + str(data) + '</div>')
