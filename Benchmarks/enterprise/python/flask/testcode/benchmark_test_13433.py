# SPDX-License-Identifier: Apache-2.0
from markupsafe import Markup
import html
from flask import request


def make_reader(raw):
    def read():
        return raw.strip()
    return read

def BenchmarkTest13433():
    user_id = request.args.get('id', '')
    reader = make_reader(user_id)
    data = reader()
    processed = html.escape(data)
    return Markup('<div>' + str(processed) + '</div>')
