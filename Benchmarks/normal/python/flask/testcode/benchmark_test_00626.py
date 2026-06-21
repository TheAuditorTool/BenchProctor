# SPDX-License-Identifier: Apache-2.0
from markupsafe import Markup
from flask import request


def BenchmarkTest00626():
    xml_value = request.get_data(as_text=True)
    data = (lambda v: v.strip())(xml_value)
    return Markup('<div>' + str(data) + '</div>')
