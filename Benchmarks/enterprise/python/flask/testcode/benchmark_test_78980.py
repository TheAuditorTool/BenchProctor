# SPDX-License-Identifier: Apache-2.0
from markupsafe import Markup
from flask import request


def BenchmarkTest78980():
    referer_value = request.headers.get('Referer', '')
    data = str(referer_value).replace('\x00', '')
    return Markup('<div>' + str(data) + '</div>')
