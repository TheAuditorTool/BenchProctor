# SPDX-License-Identifier: Apache-2.0
from markupsafe import Markup
from flask import request


def BenchmarkTest02635():
    auth_header = request.headers.get('Authorization', '')
    return Markup('<div>' + str(auth_header) + '</div>')
