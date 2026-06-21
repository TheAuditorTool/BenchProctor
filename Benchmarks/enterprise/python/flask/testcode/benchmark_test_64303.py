# SPDX-License-Identifier: Apache-2.0
from markupsafe import Markup
import html
from flask import request


def BenchmarkTest64303():
    xml_value = request.get_data(as_text=True)
    data = xml_value if xml_value else 'default'
    processed = html.escape(data)
    return Markup('<div>' + str(processed) + '</div>')
