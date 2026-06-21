# SPDX-License-Identifier: Apache-2.0
from markupsafe import Markup
import html
from flask import request


def make_reader(raw):
    def read():
        return raw.strip()
    return read

def BenchmarkTest00587():
    raw_body = request.get_data(as_text=True)
    reader = make_reader(raw_body)
    data = reader()
    processed = html.escape(data)
    return Markup('<img src="' + str(processed) + '">')
