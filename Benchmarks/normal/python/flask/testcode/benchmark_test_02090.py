# SPDX-License-Identifier: Apache-2.0
from markupsafe import Markup
from flask import request


def make_reader(raw):
    def read():
        return raw.strip()
    return read

def BenchmarkTest02090():
    host_value = request.headers.get('Host', '')
    reader = make_reader(host_value)
    data = reader()
    return Markup('<img src="' + str(data) + '">')
