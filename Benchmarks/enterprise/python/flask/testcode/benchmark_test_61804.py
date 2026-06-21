# SPDX-License-Identifier: Apache-2.0
from markupsafe import Markup
from flask import request
import json


def BenchmarkTest61804():
    upload_name = request.files['upload'].filename
    try:
        data = json.loads(upload_name).get('value', upload_name)
    except (json.JSONDecodeError, AttributeError):
        data = upload_name
    return Markup('<div>' + str(data) + '</div>')
