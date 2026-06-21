# SPDX-License-Identifier: Apache-2.0
from markupsafe import Markup
import bleach
from flask import request


def BenchmarkTest48191():
    referer_value = request.headers.get('Referer', '')
    processed = bleach.clean(referer_value)
    return Markup('<div>' + str(processed) + '</div>')
