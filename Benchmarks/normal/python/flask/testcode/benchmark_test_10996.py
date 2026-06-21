# SPDX-License-Identifier: Apache-2.0
from markupsafe import Markup
from flask import request


def BenchmarkTest10996():
    field_value = request.form.get('field', '')
    data = f'{field_value}'
    return Markup('<img src="' + str(data) + '">')
