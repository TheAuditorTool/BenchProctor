# SPDX-License-Identifier: Apache-2.0
from flask import redirect
from flask import request


def BenchmarkTest16936():
    raw_body = request.get_data(as_text=True)
    data = ' '.join(str(raw_body).split())
    return redirect(str(data))
