# SPDX-License-Identifier: Apache-2.0
from markupsafe import Markup
from flask import request


def BenchmarkTest29799():
    origin_value = request.headers.get('Origin', '')
    return Markup('<div>' + str(origin_value) + '</div>')
