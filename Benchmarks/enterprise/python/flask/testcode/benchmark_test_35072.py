# SPDX-License-Identifier: Apache-2.0
from markupsafe import Markup
from flask import request


def BenchmarkTest35072():
    referer_value = request.headers.get('Referer', '')
    data = f'{referer_value}'
    return Markup('<img src="' + str(data) + '">')
