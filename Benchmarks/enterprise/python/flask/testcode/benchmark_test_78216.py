# SPDX-License-Identifier: Apache-2.0
from flask import request
from flask import redirect
import urllib.parse


def BenchmarkTest78216():
    upload_name = request.files['upload'].filename
    if upload_name:
        data = upload_name
    else:
        data = ''
    target = '/dashboard?hidden_field=' + urllib.parse.quote(str(data))
    return redirect(target)
