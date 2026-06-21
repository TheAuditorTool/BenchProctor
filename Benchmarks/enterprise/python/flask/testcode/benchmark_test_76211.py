# SPDX-License-Identifier: Apache-2.0
from flask import render_template_string
from flask import request
import json


def BenchmarkTest76211():
    xml_value = request.get_data(as_text=True)
    try:
        data = json.loads(xml_value).get('value', xml_value)
    except (json.JSONDecodeError, AttributeError):
        data = xml_value
    return render_template_string(data)
