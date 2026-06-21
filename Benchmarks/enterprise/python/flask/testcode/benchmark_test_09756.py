# SPDX-License-Identifier: Apache-2.0
from markupsafe import Markup
from flask import request


def BenchmarkTest09756():
    referer_value = request.headers.get('Referer', '')
    return Markup('<div>' + str(referer_value) + '</div>')
