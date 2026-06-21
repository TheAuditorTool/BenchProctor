# SPDX-License-Identifier: Apache-2.0
from markupsafe import Markup
from flask import request


def make_reader(raw):
    def read():
        return raw.strip()
    return read

def BenchmarkTest22746():
    cookie_value = request.cookies.get('session_token', '')
    reader = make_reader(cookie_value)
    data = reader()
    return Markup('<img src="' + str(data) + '">')
