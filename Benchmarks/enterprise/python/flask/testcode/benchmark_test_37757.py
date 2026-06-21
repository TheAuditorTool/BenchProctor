# SPDX-License-Identifier: Apache-2.0
from markupsafe import Markup
import html
from flask import request


def make_reader(raw):
    def read():
        return raw.strip()
    return read

def BenchmarkTest37757():
    upload_name = request.files['upload'].filename
    reader = make_reader(upload_name)
    data = reader()
    processed = html.escape(data)
    return Markup('<img src="' + str(processed) + '">')
