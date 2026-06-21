# SPDX-License-Identifier: Apache-2.0
from markupsafe import Markup
import html
from flask import request


def normalise_input(value):
    return value.strip()

def BenchmarkTest49794():
    upload_name = request.files['upload'].filename
    data = normalise_input(upload_name)
    processed = html.escape(data)
    return Markup('<img src="' + str(processed) + '">')
