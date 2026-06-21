# SPDX-License-Identifier: Apache-2.0
from markupsafe import Markup
from flask import request


def BenchmarkTest35505():
    origin_value = request.headers.get('Origin', '')
    data = ' '.join(str(origin_value).split())
    return Markup('<div>' + str(data) + '</div>')
