# SPDX-License-Identifier: Apache-2.0
from flask import redirect
from flask import request


def BenchmarkTest24943():
    raw_body = request.get_data(as_text=True)
    data = raw_body if raw_body else 'default'
    return redirect(str(data))
