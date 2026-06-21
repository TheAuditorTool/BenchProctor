# SPDX-License-Identifier: Apache-2.0
from flask import request
from flask import redirect
import urllib.parse


def make_reader(raw):
    def read():
        return raw.strip()
    return read

def BenchmarkTest14583():
    raw_body = request.get_data(as_text=True)
    reader = make_reader(raw_body)
    data = reader()
    target = '/dashboard?hidden_field=' + urllib.parse.quote(str(data))
    return redirect(target)
