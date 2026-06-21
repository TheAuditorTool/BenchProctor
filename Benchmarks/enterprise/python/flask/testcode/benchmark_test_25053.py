# SPDX-License-Identifier: Apache-2.0
from markupsafe import Markup
import html
from flask import request


def BenchmarkTest25053():
    raw_body = request.get_data(as_text=True)
    data = f'{raw_body:.200s}'
    processed = html.escape(data)
    return Markup('<img src="' + str(processed) + '">')
