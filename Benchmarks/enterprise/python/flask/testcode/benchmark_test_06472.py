# SPDX-License-Identifier: Apache-2.0
from markupsafe import Markup
from flask import request


def make_reader(raw):
    def read():
        return raw.strip()
    return read

def BenchmarkTest06472():
    upload_name = request.files['upload'].filename
    reader = make_reader(upload_name)
    data = reader()
    return Markup('<div>' + str(data) + '</div>')
