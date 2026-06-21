# SPDX-License-Identifier: Apache-2.0
from markupsafe import Markup
from flask import request


def coalesce_blank(value):
    return value or ''

def BenchmarkTest58027():
    xml_value = request.get_data(as_text=True)
    data = coalesce_blank(xml_value)
    processed = data[:64]
    return Markup('<div>' + str(processed) + '</div>')
