# SPDX-License-Identifier: Apache-2.0
from flask import redirect
from flask import request


def make_reader(raw):
    def read():
        return raw.strip()
    return read

def BenchmarkTest22666():
    multipart_value = request.form.get('multipart_field', '')
    reader = make_reader(multipart_value)
    data = reader()
    return redirect(str(data))
