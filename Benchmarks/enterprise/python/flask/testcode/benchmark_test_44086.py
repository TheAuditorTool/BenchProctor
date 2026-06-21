# SPDX-License-Identifier: Apache-2.0
from markupsafe import Markup
from flask import request


def BenchmarkTest44086():
    forwarded_ip = request.headers.get('X-Forwarded-For', '')
    return Markup('<div>' + str(forwarded_ip) + '</div>')
