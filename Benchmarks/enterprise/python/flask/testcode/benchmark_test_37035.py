# SPDX-License-Identifier: Apache-2.0
from markupsafe import Markup
from flask import request


def BenchmarkTest37035():
    json_value = (request.get_json(silent=True) or {}).get('payload', '')
    return Markup('<div>' + str(json_value) + '</div>')
