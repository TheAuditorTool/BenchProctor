# SPDX-License-Identifier: Apache-2.0
from flask import redirect
from flask import request


def BenchmarkTest45528():
    multipart_value = request.form.get('multipart_field', '')
    parts = []
    for token in str(multipart_value).split(','):
        parts.append(token.strip())
    data = ','.join(parts)
    return redirect(str(data))
