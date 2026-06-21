# SPDX-License-Identifier: Apache-2.0
from markupsafe import Markup
from flask import request


def BenchmarkTest80897():
    raw_body = request.get_data(as_text=True)
    data = ' '.join(str(raw_body).split())
    return Markup('<div>' + str(data) + '</div>')
