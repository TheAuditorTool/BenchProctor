# SPDX-License-Identifier: Apache-2.0
from urllib.parse import unquote
from flask import request


def BenchmarkTest62810():
    field_value = request.form.get('field', '')
    data = unquote(field_value)
    with open('/var/app/data/' + str(data), 'r') as fh:
        content = fh.read()
    return content
