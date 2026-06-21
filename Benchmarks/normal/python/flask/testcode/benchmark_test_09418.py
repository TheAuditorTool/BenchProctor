# SPDX-License-Identifier: Apache-2.0
from markupsafe import Markup
import html
from flask import request


def BenchmarkTest09418():
    xml_value = request.get_data(as_text=True)
    data = '{}'.format(xml_value)
    processed = html.escape(data)
    return Markup('<div>' + str(processed) + '</div>')
