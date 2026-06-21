# SPDX-License-Identifier: Apache-2.0
from markupsafe import Markup
from flask import request


def BenchmarkTest48061():
    host_value = request.headers.get('Host', '')
    return Markup('<div>' + str(host_value) + '</div>')
