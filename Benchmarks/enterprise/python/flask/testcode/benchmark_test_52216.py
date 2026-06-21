# SPDX-License-Identifier: Apache-2.0
from flask import redirect
from urllib.parse import unquote
from flask import request


def BenchmarkTest52216():
    multipart_value = request.form.get('multipart_field', '')
    data = unquote(multipart_value)
    return redirect(str(data))
