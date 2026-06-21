# SPDX-License-Identifier: Apache-2.0
from markupsafe import Markup
import html
from flask import request
import json


def BenchmarkTest10085():
    upload_name = request.files['upload'].filename
    try:
        data = json.loads(upload_name).get('value', upload_name)
    except (json.JSONDecodeError, AttributeError):
        data = upload_name
    processed = html.escape(data)
    return Markup('<img src="' + str(processed) + '">')
