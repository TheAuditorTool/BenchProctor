# SPDX-License-Identifier: Apache-2.0
from flask import redirect
from flask import request


def BenchmarkTest72763():
    field_value = request.form.get('field', '')
    return redirect(str(field_value))
