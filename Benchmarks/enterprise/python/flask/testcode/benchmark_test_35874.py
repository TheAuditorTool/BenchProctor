# SPDX-License-Identifier: Apache-2.0
from flask import request
from flask import redirect
import urllib.parse


def BenchmarkTest35874():
    upload_name = request.files['upload'].filename
    target = '/dashboard?hidden_field=' + urllib.parse.quote(str(upload_name))
    return redirect(target)
