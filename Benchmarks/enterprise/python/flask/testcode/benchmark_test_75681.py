# SPDX-License-Identifier: Apache-2.0
from markupsafe import Markup
from flask import request


def BenchmarkTest75681():
    raw_body = request.get_data(as_text=True)
    data = raw_body if raw_body else 'default'
    return Markup('<div>' + str(data) + '</div>')
