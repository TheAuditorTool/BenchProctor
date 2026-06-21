# SPDX-License-Identifier: Apache-2.0
from markupsafe import Markup
from flask import request


def BenchmarkTest33578():
    raw_body = request.get_data(as_text=True)
    data = '{}'.format(raw_body)
    return Markup('<div>' + str(data) + '</div>')
