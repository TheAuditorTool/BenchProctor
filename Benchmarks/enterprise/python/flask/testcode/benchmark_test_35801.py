# SPDX-License-Identifier: Apache-2.0
from markupsafe import Markup
from flask import request


def BenchmarkTest35801():
    origin_value = request.headers.get('Origin', '')
    data = f'{origin_value:.200s}'
    return Markup('<div>' + str(data) + '</div>')
