# SPDX-License-Identifier: Apache-2.0
from markupsafe import Markup
from urllib.parse import unquote
from flask import request


def BenchmarkTest22809():
    referer_value = request.headers.get('Referer', '')
    data = unquote(referer_value)
    return Markup('<img src="' + str(data) + '">')
