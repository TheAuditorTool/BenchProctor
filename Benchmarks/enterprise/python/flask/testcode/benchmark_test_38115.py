# SPDX-License-Identifier: Apache-2.0
from markupsafe import Markup
from flask import request


def BenchmarkTest38115():
    raw_body = request.get_data(as_text=True)
    data = raw_body.decode('utf-8', 'ignore') if isinstance(raw_body, bytes) else raw_body
    return Markup('<div>' + str(data) + '</div>')
