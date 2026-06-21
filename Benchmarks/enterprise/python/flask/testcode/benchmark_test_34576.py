# SPDX-License-Identifier: Apache-2.0
from markupsafe import Markup
from flask import request


def BenchmarkTest34576():
    json_value = (request.get_json(silent=True) or {}).get('payload', '')
    return Markup('<img src="' + str(json_value) + '">')
