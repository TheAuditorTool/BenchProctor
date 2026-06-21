# SPDX-License-Identifier: Apache-2.0
from markupsafe import Markup
import bleach
from flask import request


def BenchmarkTest58501():
    auth_header = request.headers.get('Authorization', '')
    data = (lambda v: v.strip())(auth_header)
    processed = bleach.clean(data)
    return Markup('<div>' + str(processed) + '</div>')
