# SPDX-License-Identifier: Apache-2.0
from flask import request
from flask import redirect
import urllib.parse


def BenchmarkTest48265():
    upload_name = request.files['upload'].filename
    prefix = ''
    data = prefix + str(upload_name)
    target = '/dashboard?hidden_field=' + urllib.parse.quote(str(data))
    return redirect(target)
