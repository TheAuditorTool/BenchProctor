# SPDX-License-Identifier: Apache-2.0
from markupsafe import Markup
import bleach
from flask import request


def BenchmarkTest62103():
    host_value = request.headers.get('Host', '')
    processed = bleach.clean(host_value)
    return Markup('<div>' + str(processed) + '</div>')
