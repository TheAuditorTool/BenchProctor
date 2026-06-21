# SPDX-License-Identifier: Apache-2.0
from markupsafe import Markup
from flask import request


def BenchmarkTest43624():
    raw_body = request.get_data(as_text=True)
    data = str(raw_body).replace('\x00', '')
    return Markup('<div>' + str(data) + '</div>')
