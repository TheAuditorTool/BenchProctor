# SPDX-License-Identifier: Apache-2.0
from markupsafe import Markup
import markdown
import bleach
from flask import request


def make_reader(raw):
    def read():
        return raw.strip()
    return read

def BenchmarkTest11741():
    referer_value = request.headers.get('Referer', '')
    reader = make_reader(referer_value)
    data = reader()
    processed = bleach.clean(markdown.markdown(data))
    return Markup('<div>' + str(processed) + '</div>')
