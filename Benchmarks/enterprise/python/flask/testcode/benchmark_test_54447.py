# SPDX-License-Identifier: Apache-2.0
from markupsafe import Markup
import bleach
from flask import request


def make_reader(raw):
    def read():
        return raw.strip()
    return read

def BenchmarkTest54447():
    auth_header = request.headers.get('Authorization', '')
    reader = make_reader(auth_header)
    data = reader()
    processed = bleach.clean(data)
    return Markup('<div>' + str(processed) + '</div>')
