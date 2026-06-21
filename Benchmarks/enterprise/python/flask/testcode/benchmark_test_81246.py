# SPDX-License-Identifier: Apache-2.0
from markupsafe import Markup
import html
from flask import request


def BenchmarkTest81246():
    xml_value = request.get_data(as_text=True)
    data = f'{xml_value:.200s}'
    processed = html.escape(data)
    return Markup('<img src="' + str(processed) + '">')
