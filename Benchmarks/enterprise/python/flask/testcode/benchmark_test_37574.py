# SPDX-License-Identifier: Apache-2.0
from markupsafe import Markup
from flask import request


def make_reader(raw):
    def read():
        return raw.strip()
    return read

def BenchmarkTest37574():
    auth_header = request.headers.get('Authorization', '')
    reader = make_reader(auth_header)
    data = reader()
    return Markup('<div>' + str(data) + '</div>')
