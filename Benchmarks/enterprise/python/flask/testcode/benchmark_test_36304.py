# SPDX-License-Identifier: Apache-2.0
from markupsafe import Markup
import html
from flask import request


def BenchmarkTest36304():
    referer_value = request.headers.get('Referer', '')
    data = str(referer_value).replace('\x00', '')
    processed = html.escape(data)
    return Markup('<img src="' + str(processed) + '">')
