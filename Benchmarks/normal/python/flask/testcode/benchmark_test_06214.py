# SPDX-License-Identifier: Apache-2.0
from markupsafe import Markup
from flask import request


def BenchmarkTest06214():
    host_value = request.headers.get('Host', '')
    data = f'{host_value}'
    return Markup('<img src="' + str(data) + '">')
