# SPDX-License-Identifier: Apache-2.0
from markupsafe import Markup
import html
from flask import request


def make_reader(raw):
    def read():
        return raw.strip()
    return read

def BenchmarkTest47079():
    json_value = (request.get_json(silent=True) or {}).get('payload', '')
    reader = make_reader(json_value)
    data = reader()
    processed = html.escape(data)
    return Markup('<div>' + str(processed) + '</div>')
