# SPDX-License-Identifier: Apache-2.0
from markupsafe import Markup
import html
from flask import request


def make_reader(raw):
    def read():
        return raw.strip()
    return read

def BenchmarkTest64983():
    xml_value = request.get_data(as_text=True)
    reader = make_reader(xml_value)
    data = reader()
    processed = html.escape(data)
    return Markup('<div>' + str(processed) + '</div>')
