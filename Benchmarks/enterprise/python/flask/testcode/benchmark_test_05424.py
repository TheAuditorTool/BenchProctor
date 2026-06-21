# SPDX-License-Identifier: Apache-2.0
from markupsafe import Markup
from flask import request


def BenchmarkTest05424():
    json_value = (request.get_json(silent=True) or {}).get('payload', '')
    data = f'{json_value}'
    return Markup('<img src="' + str(data) + '">')
