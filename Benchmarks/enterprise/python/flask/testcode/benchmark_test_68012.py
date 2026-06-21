# SPDX-License-Identifier: Apache-2.0
from markupsafe import Markup
import html
from flask import request


def BenchmarkTest68012():
    xml_value = request.get_data(as_text=True)
    data = ' '.join(str(xml_value).split())
    processed = html.escape(data)
    return Markup('<img src="' + str(processed) + '">')
