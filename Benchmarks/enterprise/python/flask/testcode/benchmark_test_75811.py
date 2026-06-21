# SPDX-License-Identifier: Apache-2.0
from markupsafe import Markup
import json
from flask import request


def BenchmarkTest75811():
    raw_body = request.get_data(as_text=True)
    data = json.loads(raw_body).get('value', '')
    return Markup('<div>' + str(data) + '</div>')
