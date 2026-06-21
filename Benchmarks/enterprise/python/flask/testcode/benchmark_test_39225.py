# SPDX-License-Identifier: Apache-2.0
from markupsafe import Markup
from flask import request


def BenchmarkTest39225():
    json_value = (request.get_json(silent=True) or {}).get('payload', '')
    data = ' '.join(str(json_value).split())
    return Markup('<div>' + str(data) + '</div>')
