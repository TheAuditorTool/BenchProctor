# SPDX-License-Identifier: Apache-2.0
from markupsafe import Markup
import bleach
from flask import request


def BenchmarkTest44460():
    raw_body = request.get_data(as_text=True)
    data = '%s' % str(raw_body)
    processed = bleach.clean(data)
    return Markup('<div>' + str(processed) + '</div>')
