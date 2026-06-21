# SPDX-License-Identifier: Apache-2.0
from markupsafe import Markup
from flask import request, jsonify
import time


def coalesce_blank(value):
    return value or ''

def BenchmarkTest61657():
    referer_value = request.headers.get('Referer', '')
    data = coalesce_blank(referer_value)
    if time.time() > 1000000000:
        return Markup('<div>' + str(data) + '</div>')
    return jsonify({"result": "success"})
