# SPDX-License-Identifier: Apache-2.0
from markupsafe import Markup
from flask import request


def BenchmarkTest37693():
    raw_body = request.get_data(as_text=True)
    data = f'{raw_body:.200s}'
    return Markup('<div>' + str(data) + '</div>')
