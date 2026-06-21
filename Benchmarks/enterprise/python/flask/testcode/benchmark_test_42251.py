# SPDX-License-Identifier: Apache-2.0
from flask import redirect
from flask import request


def BenchmarkTest42251():
    upload_name = request.files['upload'].filename
    data = ' '.join(str(upload_name).split())
    return redirect(str(data))
