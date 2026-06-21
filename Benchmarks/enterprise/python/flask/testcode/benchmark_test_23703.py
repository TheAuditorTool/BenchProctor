# SPDX-License-Identifier: Apache-2.0
from flask import redirect
from flask import request


def make_reader(raw):
    def read():
        return raw.strip()
    return read

def BenchmarkTest23703():
    origin_value = request.headers.get('Origin', '')
    reader = make_reader(origin_value)
    data = reader()
    return redirect(str(data))
