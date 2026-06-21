# SPDX-License-Identifier: Apache-2.0
from flask import redirect
from flask import request


def BenchmarkTest07202():
    raw_body = request.get_data(as_text=True)
    data = f'{raw_body}'
    return redirect(str(data))
