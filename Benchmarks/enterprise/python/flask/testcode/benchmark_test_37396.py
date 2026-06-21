# SPDX-License-Identifier: Apache-2.0
from flask import redirect
from flask import request
import json


def BenchmarkTest37396():
    upload_name = request.files['upload'].filename
    try:
        data = json.loads(upload_name).get('value', upload_name)
    except (json.JSONDecodeError, AttributeError):
        data = upload_name
    return redirect(str(data))
