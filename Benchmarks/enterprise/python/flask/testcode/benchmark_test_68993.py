# SPDX-License-Identifier: Apache-2.0
from markupsafe import Markup
import html
from flask import request


def make_reader(raw):
    def read():
        return raw.strip()
    return read

def BenchmarkTest68993():
    origin_value = request.headers.get('Origin', '')
    reader = make_reader(origin_value)
    data = reader()
    processed = html.escape(data)
    return Markup('<div>' + str(processed) + '</div>')
