# SPDX-License-Identifier: Apache-2.0
from markupsafe import Markup
import json
from flask import request
from flask import render_template_string


def BenchmarkTest12278():
    raw_body = request.get_data(as_text=True)
    data = json.loads(raw_body).get('value', '')
    return render_template_string('{{ value }}', value=data)
