# SPDX-License-Identifier: Apache-2.0
from flask import redirect
from flask import request


def BenchmarkTest65780():
    multipart_value = request.form.get('multipart_field', '')
    data = f'{multipart_value:.200s}'
    return redirect(str(data))
