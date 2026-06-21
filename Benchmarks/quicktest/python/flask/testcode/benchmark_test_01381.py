# SPDX-License-Identifier: Apache-2.0
from flask import render_template_string
from flask import request
import json


def BenchmarkTest01381():
    upload_name = request.files['upload'].filename
    try:
        data = json.loads(upload_name).get('value', upload_name)
    except (json.JSONDecodeError, AttributeError):
        data = upload_name
    return render_template_string(data)
