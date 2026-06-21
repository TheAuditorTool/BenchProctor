# SPDX-License-Identifier: Apache-2.0
from markupsafe import Markup
from flask import request


def BenchmarkTest56072():
    referer_value = request.headers.get('Referer', '')
    data = f'{referer_value:.200s}'
    return Markup('<div>' + str(data) + '</div>')
