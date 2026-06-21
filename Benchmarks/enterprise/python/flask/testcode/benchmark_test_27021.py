# SPDX-License-Identifier: Apache-2.0
from markupsafe import Markup
from flask import request


def BenchmarkTest27021():
    raw_body = request.get_data(as_text=True)
    return Markup('<img src="' + str(raw_body) + '">')
