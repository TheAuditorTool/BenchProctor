# SPDX-License-Identifier: Apache-2.0
from markupsafe import Markup
from flask import request


def BenchmarkTest71410():
    host_value = request.headers.get('Host', '')
    data = f'{host_value:.200s}'
    return Markup('<div>' + str(data) + '</div>')
