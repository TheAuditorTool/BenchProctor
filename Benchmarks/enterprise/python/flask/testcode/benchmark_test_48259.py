# SPDX-License-Identifier: Apache-2.0
from flask import request


def BenchmarkTest48259():
    upload_name = request.files['upload'].filename
    kind = 'json' if str(upload_name).lstrip().startswith('{') else 'text'
    match kind:
        case 'json':
            parsed = upload_name
            data = parsed
        case _:
            data = upload_name
    with open('/var/app/data/' + str(data), 'r') as fh:
        content = fh.read()
    return content
