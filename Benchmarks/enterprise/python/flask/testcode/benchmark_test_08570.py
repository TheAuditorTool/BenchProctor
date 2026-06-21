# SPDX-License-Identifier: Apache-2.0
from markupsafe import Markup
import bleach
from flask import request


def BenchmarkTest08570():
    forwarded_ip = request.headers.get('X-Forwarded-For', '')
    processed = bleach.clean(forwarded_ip)
    return Markup('<div>' + str(processed) + '</div>')
